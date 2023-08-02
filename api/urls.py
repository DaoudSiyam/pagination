from django.urls import path
from . import views

urlpatterns = [
    path('',views.api_overview, name= 'api-overview'),
    path('videos-list/',views.VideosListView.as_view(), name= 'videos-list'),
    path('video-details/<int:pk>/',views.video_details, name= 'video-details'),
    path('videos-list/action-category',views.action_category, name= 'action-category'),
    path('videos-list/comedy-category',views.comedy_category, name= 'comedy-category'),
    path('videos-list/tutorial-category',views.tutorial_category, name= 'tutorial-category'),
    path('videos-list/educational-category',views.educational_category, name= 'educational-category'),
    path('videos-list/entertainment-category',views.entertainment_category, name= 'entertainment-category'),
    path('videos-list/music-category',views.music_category, name= 'music-category'),
]