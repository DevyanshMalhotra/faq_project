from rest_framework import generics
from rest_framework.response import Response
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

class FAQListAPIView(generics.ListAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        return FAQ.objects.all()

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')
        cache_key = f"faqs_{lang}"
        data = cache.get(cache_key)
        if not data:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True, context={'lang': lang})
            data = serializer.data
            cache.set(cache_key, data, timeout=60)
        return Response(data)
