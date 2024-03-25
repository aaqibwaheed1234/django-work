from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import JsonResponse
from .models import Message
# Create your views here.

# def index(request):
#     return render(request, "chat/index.html")

class IndexView(TemplateView):
    template_name = "room/index.html"

class RoomView(View):
    def get(self, request, *args, **kwargs):
        room_name = kwargs['room_name']
        return render(request, "room/room.html", {"room_name": room_name})  
    
class MessageView(View):
    def post(self, request, *args, **kwargs):
        room_name = request.POST.get('room_name')
        user = request.user
        content = request.POST.get('message')
        message = Message.objects.create(room=room_name, user=user, content=content)
        return JsonResponse({'success': True})

# class RoomView(TemplateView):
#     template_name = "room/room.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['room_name'] = kwargs['room_name']
#         return context
    

