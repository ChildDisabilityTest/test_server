from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'tester', TesterViewSet)
router.register(r'child', ChildViewSet)
router.register(r'incheon', IncheonRegionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('gulist/', GuList.as_view()),
    path('emdlist/', Emdlist.as_view()),
]