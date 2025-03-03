from sentence_transformers import SentenceTransformer
from pgvector.django import CosineDistance
from store.models import Store, StoreItem
from .models import StoreEmbedding, StoreItemEmbedding


embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", cache_folder="./models")

def generate_embedding(text):
    return embedding_model.encode(text).tolist()

def update_store_embedding(store):
    vector = generate_embedding(store.description)
    StoreEmbedding.objects.update_or_create(store=store, defaults={"description_vector": vector})

def update_store_item_embedding(store_item):
    vector = generate_embedding(store_item.description)
    StoreItemEmbedding.objects.update_or_create(store_item=store_item, defaults={"description_vector": vector})

def search_stores(query, top_n=5):
    query_vector = generate_embedding(query)
    return Store.objects.annotate(
        similarity=CosineDistance("embedding__description_vector", query_vector)
    ).order_by("similarity")[:top_n]

def search_store_items(query, top_n=5):
    query_vector = generate_embedding(query)
    return StoreItem.objects.annotate(
        similarity=CosineDistance("embedding__description_vector", query_vector)
    ).order_by("similarity")[:top_n]
