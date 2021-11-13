
from django.urls import path

from postApp import views
from postApp.views.postView import PostlistCreateView, PostDetailView

urlpatterns = [
    path('posts/',views.PostlistCreateView.as_view()),
    path('post/<int:pk>/',views.PostDetailView.as_view()),
]
