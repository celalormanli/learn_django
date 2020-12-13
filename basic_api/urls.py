from rest_framework import routers
from .api import BasicApiViewSet

router = routers.DefaultRouter()  
router.register('api/basic_api', BasicApiViewSet,'basic_api')



urlpatterns = router.urls 