from django.urls import path

from postApp import views
from postApp.views.postView import PostCreateView, PostView, ProductoDeleteView,\
                         ProductoUpdateView

urlpatterns = [
    path('posts/',views.PostCreateView.as_view()),
    path('post/<int:user>/',views.PostView.as_view()),
    path('post/delete/<int:user>/<int:pk>/',views.ProductoDeleteView.as_view()),
    path('post/update/<int:user>/<int:pk>/',views.ProductoUpdateView.as_view()),
]
