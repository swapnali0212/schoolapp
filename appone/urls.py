from rest_framework.routers import SimpleRouter
from appone.views import *
router =SimpleRouter()
router.register('api/v1', StudentOps)
router.register('api/v2',UserProfiOps)

urlpatterns = router.urls