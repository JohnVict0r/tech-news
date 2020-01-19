from rest_framework import serializers
from tech.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'post_url', 'img_url', 'published_date')