from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from listings import views


router = routers.DefaultRouter()
router.register(r'', views.ListingViewSet)


urlpatterns = [
    path('api/v1/units/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
