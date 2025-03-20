from .views import SnippetViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'snippets', SnippetViewSet)

urlpatterns = router.urls
