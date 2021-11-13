from rest_framework                       import generics, views
from postApp.models.post                  import Post
from postApp.serializers.postSerializer   import PostSerializer


# List, create 
class PostlistCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Modifica y elimina las publicaciones
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


