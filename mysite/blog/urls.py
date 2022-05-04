from django.urls import path
from blog import views

urlpatterns = [
    path('post/draft/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<str:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<str:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<str:pk>/', views.AboutView.as_view(), name='post_detail'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('', views.PostListView.as_view(), name='post_list'),
]
