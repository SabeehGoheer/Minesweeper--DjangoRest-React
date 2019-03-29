from .views import BoardMapViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BoardMapViewSet, basename='BoardMap')
urlpatterns = router.urls


# from django.urls import path
# from .views import BoardMapListView, BoardMapDetailView, BoardMapUpdateView

# urlpatterns = [
#     path('', BoardMapListView.as_view()), 
#     path('<pk>/update/', BoardMapUpdateView.as_view()),
#     path('<pk>', BoardMapDetailView.as_view())
# ]
