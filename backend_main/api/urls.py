from django.urls import path
from .views import VideoListView, VideoUploadView, SingleVideoView
from .views import register_user, login_user
from .views import CommentListCreateView


urlpatterns = [
    path('videos/', VideoListView.as_view(), name='video-list'),
    path('videos/upload/', VideoUploadView.as_view(), name='video-upload'),
    path('videos/<int:id>/', SingleVideoView.as_view(), name='video-detail'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('videos/<int:video_id>/comments/', CommentListCreateView.as_view(), name='comments'),

]
