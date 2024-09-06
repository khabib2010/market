from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serial import UserSerial ,CategorySerial ,Change_password ,Productserial,Savatserial
from .models import User ,Category ,Product ,Product_imgs


class MyTokenView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        print(username, password)
        user = User.objects.filter(username=username).last()
        print(user)
        if user and user.check_password(password):
            tokens = RefreshToken.for_user(user=user)
            message = {
                "refresh": str(tokens),
                'access': str(tokens.access_token),
                'username': user.username,
                'user_id': user.id,
                'status': user.status
            }
            return Response(message)
        return Response({
            'message': 'username yoki parol xato kiritildi.. '
        })

class UserCreateListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerial


class UserDetailview(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerial
    lookup_field = 'id'

class CategoryCreate(ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerial

class Change_password(APIView):
    def post(self , request):
        serializer=Change_password(data=request.data)
        if serializer.is_valid():
            old_p=request.data['old_password']
            if request.user.check_password(old_p):
                d=request.data
                if d['new_password']==d['confirm_password']:
                    request.user.set_password(d['new_password'])
                    request.save()
            else:
                return Response({'message':'eski parolni kiritnig'})
        return Response(serializer.errors)



class Productcreate(APIView):
    def post(self, request):
        serializer = Productserial(data=request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
        
            return Response({'message':'Ok'})
        return Response({'message':'kiritishda hatolik'})


class Savatcreate(APIView):
    def post(self,request):
        serializer=Savatserial(data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'ok'})
        return Response({'message':'kiritishda hatolik'})


class Product_detail_view(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserial
    lookup_field='id'

class Category_detail_view(RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerial
    lookup_field='id'