from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import VideoSerializer
from base.models import Video

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List' : '/videos-list/',
        'Detail View' : '/video-details/<str:pk>/', 
    }
    return Response(api_urls)


class VideosListView(ListAPIView):
    queryset = Video.objects.all().order_by('-id')
    serializer_class = VideoSerializer
    

@api_view(['GET'])
def video_details(request , pk):
    video = Video.objects.get( id = pk )
    serializer = VideoSerializer(video)

    return Response(serializer.data)


@api_view(['GET'])
def action_category(resuest):
    videos = Video.objects.filter( category = 'Action' ).order_by('-id')
    serializer = VideoSerializer(videos, many = True)
    print(serializer.data)

    return Response(serializer.data)


@api_view(['GET'])
def comedy_category(resuest):
    videos = Video.objects.filter( category = 'Comedy' ).order_by('-id')
    serializer = VideoSerializer(videos, many = True)

    return Response(serializer.data)


@api_view(['GET'])
def tutorial_category(resuest):
    videos = Video.objects.filter( category = 'Tutorial').order_by('-id')
    serializer = VideoSerializer(videos, many = True)

    return Response(serializer.data)


@api_view(['GET'])
def educational_category(resuest):
    videos = Video.objects.filter( category = 'Educational').order_by('-id')
    serializer = VideoSerializer(videos, many = True)

    return Response(serializer.data)


@api_view(['GET'])
def entertainment_category(resuest):
    videos = Video.objects.filter( category = 'Entertainment').order_by('-id')
    serializer = VideoSerializer(videos, many = True)

    return Response(serializer.data)


@api_view(['GET'])
def music_category(resuest):
    videos = Video.objects.filter( category = 'Music' ).order_by('-id')
    serializer = VideoSerializer(videos, many = True)

    return Response(serializer.data)

