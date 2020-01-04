from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView  # , TokenRefreshView
from . import views

router = routers.DefaultRouter()
router.register(r'tags', views.TagViewSet)
router.register(r'transactions', views.TransactionViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('hi/', views.HelloView.as_view(), name='hello'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    # path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('profile/', views.CurrentUserView.as_view(), name='profile'),
]
