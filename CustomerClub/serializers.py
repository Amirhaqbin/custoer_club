from pyexpat import model
from rest_framework import serializers
from app.serializers import CustomUserSerializer
from app.models import CustomUser
from .models import Gift, Log, Profile
from rest_framework.renderers import JSONRenderer


class GiftSerializer(serializers.ModelSerializer):
    class Meta:
            model = Gift
            fields = (
                'title',
                'allowed_to_used',
                'allowed_to_used_duration',
                'image',
                'detail',
                'score',
                'slug', 
                'create_at',
                'id',
            )
            


class ProfileSerializer(serializers.ModelSerializer):
    customer = CustomUserSerializer
    class Meta:
        model = Profile
        fields = '__all__'

        # def create(self, validated_data):
        #     user_data = validated_data.pop('user')
        #     profile = Profile.objects.create(**validated_data)
        #     CustomUser.objects.create(profile=profile, **user_data)
        #     return profile
        read_only_fields = ['score_user', 'is_gold']    
        


class LogSerializer(serializers.Serializer):
    gift = GiftSerializer
    user = CustomUserSerializer

    class Meta:
        model: Log
        fields = '__all__'

        read_only_fields = '__all__'





