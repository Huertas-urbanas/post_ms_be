from postApp.models.post import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','user', 'text', 'datepublished','image']

def to_representation(self, obj):
    post = Post.objects.get(id=obj.id)

    return{
        'id' : obj.id,
        'user' : obj.user,
        'text' : obj.text,
        'image' : obj.image,
    }