from rest_framework import serializers

from .models import News


class NewsDetailSerializer(serializers.ModelSerializer):
    category_title = serializers.SerializerMethodField()

    def get_category_title(self, obj):
        return obj.category.title

    class Meta:
        model = News
        fields = '__all__'


class NewsCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    category_id = serializers.IntegerField()


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NewsDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id',)
