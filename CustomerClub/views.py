from distutils.log import Log
from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from app.models import CustomUser
from .permissions import IsSuperUserOrIs_staff, ProfilePermission
from rest_framework.views import APIView
from .models import Gift, Profile, Log
from .serializers import  GiftSerializer, ProfileSerializer, LogSerializer
from rest_framework.decorators import api_view
from django.utils import timezone
from datetime import timedelta



class GiftDetailViewset(viewsets.ModelViewSet):
    permission_class = (IsSuperUserOrIs_staff,)
    serializer_class = GiftSerializer
    queryset = Gift.objects.all()
    filterset_fields = ['title', 'allowed_to_used_duration', 'score', 'create_at']
    lookup_field = "slug"



class GiftListViewset(viewsets.ModelViewSet):
    permission_class = (IsSuperUserOrIs_staff,)
    serializer_class = GiftSerializer
    queryset = Gift.objects.order_by('-create_at')
        
class ProfileViewset(viewsets.ModelViewSet):
    permission_class = [ProfilePermission,]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()



class LogViewset(viewsets.ModelViewSet):
    permission_class = (IsSuperUserOrIs_staff,)
    serializer_class = LogSerializer
    queryset = Log.objects.all()



class ScoreView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request, pk):
        
        id_=self.kwargs['pk']
        gift=Gift.objects.get(pk=id_)
        from_dt = timezone.now() - timedelta(days=gift.allowed_to_used_duration)
        logs=Log.objects.filter(user=request.user, gift=gift, created_at__gte=from_dt)
        score_gift =gift.score
        id_user= self.request.user.id
        user_obj = Profile.objects.get(id=id_user)
        score_user = user_obj.score_user
        user_obj = CustomUser.objects.get(id=id_user)
        
        if len(logs) >= gift.allowed_to_used:
            print("error logs too much")
            return Response(status.HTTP_400_BAD_REQUEST) #response error
        
        elif score_gift > score_user :
            print("emtize kam ast")
            return Response(status.HTTP_400_BAD_REQUEST)

        else:
            print("emtize okeye")

            Log.objects.create(gift=gift, score_log=score_gift, user=user_obj)
            print("create")
            return Response( status.HTTP_201_CREATED)

    