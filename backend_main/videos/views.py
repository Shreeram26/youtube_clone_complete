from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer

class VideoListAPIView(APIView):
    def get(self, request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
