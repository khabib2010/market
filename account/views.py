from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serial import UserSerial
from .models import User


class UserCreateListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerial


class UserDetailview(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerial
    lookup_field = 'id'