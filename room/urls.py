from django.urls import path
from .views import IndexView, RoomView, MessageView


urlpatterns = [
     path('index/', IndexView.as_view(), name='index'),
     path('<str:room_name>/', RoomView.as_view(), name='room'),  
     path('messageView/', MessageView.as_view(), name='messageView'),
]