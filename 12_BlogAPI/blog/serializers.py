from rest_framework import serializers
from .models import (
    Category,
    Post,
)

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        # fields = '__all__'
        # fields = ['name']
        exclude = []

class PostSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()

    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()

    class Meta:
        model = Post
        exclude = []