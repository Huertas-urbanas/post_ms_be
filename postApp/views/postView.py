from rest_framework                       import generics, status
from postApp.models.post                  import Post
from postApp.serializers.postSerializer   import PostSerializer
from rest_framework.response import Response

# Create
class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *arg, **kwargs):

        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Publicación guardada", status=status.HTTP_201_CREATED)

# Read
class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.filter(user=self.kwargs['user'])
        return queryset

# Delete
class PostDeleteView(generics.DestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):           
        queryset = Post.objects.filter(user=self.kwargs['user'])
        return queryset

    def delete(self, request, *arg, **kwargs):        
        return super().destroy(request, *arg, **kwargs)

# Update 
class PostUpdateView(generics.UpdateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.filter(user=self.kwargs['user'])
        return queryset

    def put(self, request, *arg, **kwargs):
        return super().update(request, *arg, **kwargs)


