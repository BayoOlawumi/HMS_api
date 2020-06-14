from rest_framework import serializers
from .models import UserProfile

""" 
  email = serializers.EmailField(max_length=255)
   name = serializers.CharField(max_length=255)
   is_staff = serializers.BooleanField(default=False)
   is_active = serializers.BooleanField(default=True)

   def create(self,validated_data):
      return UserProfile.objects.create(**validated_data)

   def update(self,instance,validated_data):
       instance.email=validated_data.get('name',instance.email)
       instance.name = validated_data.get('name', instance.name)
       instance.is_active = validated_data.get('name', instance.is_active)
       instance.is_staff = validated_data.get('name', instance.is_staff)
       instance.save()
       return instance """


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=(
            'email',
            'name',
            'is_staff',
            'is_active',
        )


