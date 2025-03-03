from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .services import search_stores, search_store_items
from .serializers import StoreSearchSerializer, StoreItemSearchSerializer

class StoreSearchView(APIView):
    """Search for stores using semantic search."""
    permission_classes = [AllowAny]

    def get(self, request):
        query = request.query_params.get("q", "")
        if not query:
            return Response({"error": "Query parameter is required."}, status=400)

        stores = search_stores(query)
        serializer = StoreSearchSerializer(stores, many=True)
        return Response(serializer.data)

class StoreItemSearchView(APIView):
    """Search for store items using semantic search."""
    permission_classes = [AllowAny]

    def get(self, request):
        query = request.query_params.get("q", "")
        if not query:
            return Response({"error": "Query parameter is required."}, status=400)

        items = search_store_items(query)
        serializer = StoreItemSearchSerializer(items, many=True)
        return Response(serializer.data)
