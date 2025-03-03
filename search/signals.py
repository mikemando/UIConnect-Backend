from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .services import search_stores, search_store_items
from .serializers import StoreSearchSerializer, StoreItemSearchSerializer

class MarketplaceSearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        query = request.query_params.get("q", "")
        if not query:
            return Response({"error": "Query parameter 'q' is required."}, status=400)

        store_results = search_stores(query)
        item_results = search_store_items(query)

        store_serializer = StoreSearchSerializer(store_results, many=True)
        item_serializer = StoreItemSearchSerializer(item_results, many=True)

        combined_results = (
            [{"type": "store", **data} for data in store_serializer.data] +
            [{"type": "item", **data} for data in item_serializer.data]
        )

        return Response(combined_results)
