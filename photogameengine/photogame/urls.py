from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'pictures', views.PictureViewSet)
router.register(r'votes', views.PictureVoteViewSet)
router.register(r'views', views.PictureViewsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]