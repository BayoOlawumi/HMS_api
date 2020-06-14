from rest_framework import serializers
from .models import Room


class RoomclassSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    unique_color = serializers.CharField(max_length=15)
    price = serializers.DecimalField(max_digits=9,decimal_places=2)

    def create(self,validated_data):
       return Room.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.unique_color = validated_data.get('unique_color', instance.unique_color)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance