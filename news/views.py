from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, DestroyAPIView
from .models import Category, News
from .serializers import NewsCreateSerializer, NewsListSerializer, NewsDetailSerializer, NewsDeleteSerializer


class NewsDeleteAPIView(DestroyAPIView):
    serializer_class = NewsDeleteSerializer
    queryset = News.objects.all()


class NewsRetrieveAPIView(RetrieveAPIView):
    serializer_class = NewsDetailSerializer
    queryset = News.objects.all()


class NewsListAPIView(ListCreateAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.all()


class NewsListAPIView2(APIView):
    def get(self, request):
        news = [{'id': i.id, 'title': i.title} for i in News.objects.all()]

        return Response(news)


@api_view(['POST'])
def news_create(request):
    serializer = NewsCreateSerializer(data=request.POST)
    serializer.is_valid()

    category = Category.objects.get(id=serializer.validated_data['category_id'])

    news = News.objects.create(
        title=serializer.validated_data['title'],
        category=category,
    )

    return Response(serializer.data)
