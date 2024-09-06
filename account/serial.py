from rest_framework import serializers

from .models import User, Category ,Product, Product_imgs, Savat


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['user_id'] = user.id
        # ...
        print(token)
        return token

class UserSerial(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['username', 'password', 'photo', 'id', 'status']
        extra_kwargs = {'password': {'write_only': True}, 'status': {'read_only': True}}    

    def create(self, validated_data):
        password = validated_data.pop('password')
        user     = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class Change_password(serializers.Serializer):
    old_password = serializers.CharField(max_length=25)
    new_password = serializers.CharField(max_length=25)
    confirm_password = serializers.CharField(max_length=25)

class CategorySerial(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields=['id','name', 'rasm','parent']


class Productserial(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','batafsil','price','category']

    def create(self,validated_data):
        
        print(validated_data)
        print(self.context['request'].user)

        owner = self.context['request'].user
        new_product = Product.objects.create(**validated_data, user=owner)
        return new_product  

class Savatserial(serializers.ModelSerializer):
    class Meta:
        model=Savat
        fields=['id','soni','product']

    def create(self,validated_data):
        owner=self.context['request'].user
        new_savat=Savat.objects.create(**validated_data,user=owner)
        return new_savat


