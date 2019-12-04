from django.urls import path, include
from rest_framework import routers
from antisocial.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'neighborhoods', views.NeighborHoodViewSet)
router.register(r'contactinfo', views.ContactInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.ObtainAuthTokenAndUserDetails.as_view()),
    path('udft/', views.UserDetailsFromToken.as_view()),
    path('neighborhoods/<int:id>/contactinfo/', views.NeighborhoodContactInfoViewSet.as_view())
]
