from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from bot import views


router = routers.DefaultRouter()
router.register(f'users', views.UserViewSet)
router.register(f'messages', views.MessageHistoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(f'^', include(router.urls)),
    url(f'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))]
