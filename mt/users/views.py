from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.http import HttpResponse

User = get_user_model()

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def home(request):
    return HttpResponse("Пользователи")
