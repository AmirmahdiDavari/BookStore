from Book.API import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BookViewSet, basename='user')
urlpatterns = router.urls