from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Video
from .serializers import VideoSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Comment
from .serializers import CommentSerializer
from rest_framework import generics, permissions



class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all().order_by('-uploaded_at')
    serializer_class = VideoSerializer


class VideoUploadView(generics.CreateAPIView):
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SingleVideoView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'id'


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        video_id = self.kwargs['video_id']
        return Comment.objects.filter(video_id=video_id).order_by('-timestamp')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email', '')

    if not username or not password:
        return Response({'error': 'Username and password required'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already taken'}, status=409)

    user = User.objects.create_user(username=username, password=password, email=email)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=201)


@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response({'error': 'Invalid credentials'}, status=401)