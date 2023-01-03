
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewSet, StoreViewSet, FamilyViewSet, ImportantDayViewSet



router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'family', FamilyViewSet, basename='family')
router.register(r'imporatnt', ImportantDayViewSet, basename='importantday')
router.register(r'store', StoreViewSet, basename='store')


urlpatterns = [
    path('', include(router.urls)),
    path('token', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
]
