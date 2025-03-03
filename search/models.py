from django.db import models
from pgvector.django import VectorField
from sentence_transformers import SentenceTransformer
from store.models import Store, StoreItem

embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", cache_folder="./models")

class StoreEmbedding(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE, related_name="embedding")
    description_vector = VectorField(dimensions=384)

    @staticmethod
    def update_embedding(store):
        """Generate and store embeddings when a store is created/updated."""
        embedding, _ = StoreEmbedding.objects.get_or_create(store=store)
        embedding.description_vector = embedding_model.encode(store.description).tolist()
        embedding.save()

class StoreItemEmbedding(models.Model):
    store_item = models.OneToOneField(StoreItem, on_delete=models.CASCADE, related_name="embedding")
    description_vector = VectorField(dimensions=384)

    @staticmethod
    def update_embedding(store_item):
        """Generate and store embeddings when a store item is created/updated."""
        embedding, _ = StoreItemEmbedding.objects.get_or_create(store_item=store_item)
        embedding.description_vector = embedding_model.encode(store_item.description).tolist()
        embedding.save()
