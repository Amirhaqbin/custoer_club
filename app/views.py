from django.shortcuts import render
from rest_framework import viewsets
from CustomerClub.permissions import ProfilePermission
from .models import CustomUser, Store, FamilyMember , ImportantDate
from .serializers import CustomUserSerializer, FamilySerializer, StoreSerializer, ImportantDateSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Pastebin API')


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000




class UserViewSet(viewsets.ModelViewSet): 
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('id_number', 'last_name', 'mobile_phone', 'telephone_number', 'zip_code')
    ordering_fields = ('first_name', 'last_name', 'updated_at')
    pagination_class = StandardResultsSetPagination
    pagination_class.page_size = 10


class StoreViewSet(viewsets.ModelViewSet): 
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes =[ProfilePermission,]


class FamilyViewSet(viewsets.ModelViewSet):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilySerializer
    permission_classes =[ProfilePermission,]


class ImportantDayViewSet(viewsets.ModelViewSet):
    queryset = ImportantDate.objects.all()
    serializer_class = ImportantDateSerializer
    permission_classes =[ProfilePermission,]