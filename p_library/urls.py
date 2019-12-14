from django.contrib import admin  
from django.urls import path  
from .views import AuthorEdit, AuthorList, FriendEdit, RedactionDetailView, friend_info
  

app_name = 'p_library'  
urlpatterns = [  
    path("redactions/<str:pk>/", RedactionDetailView.as_view(), name="redaction_detail"),
    path('friend/create', FriendEdit.as_view(), name='friend_create'),
    path('friends', friend_info, name='friend_list'),
]