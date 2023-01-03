from .views import GiftDetailViewset, ScoreView, ProfileViewset, GiftListViewset, LogViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.conf.urls import url



router = DefaultRouter()
router.register(r'detail', GiftDetailViewset, basename='gift')
router.register(r'^profile', ProfileViewset, basename='profile') 
router.register(r'list', GiftListViewset, basename='list')
router.register(r'log', LogViewset, basename='log')


urlpatterns = [
    path('', include(router.urls)),
    path('score/<int:pk>/', ScoreView.as_view()),
    # path('^profile/(?P<id>[0-9]+)/$', ProfileViewset.as_view()),
] 

# <int:gift_id>/