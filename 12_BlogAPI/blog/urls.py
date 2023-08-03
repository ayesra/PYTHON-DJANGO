# from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import CategoryView, PostView

# ROUTER:
router = DefaultRouter()
router.register('category', CategoryView)
router.register('post', PostView)

# urlpatterns = [
#     path('', include('router.urls'))
# ]
urlpatterns = router.urls
