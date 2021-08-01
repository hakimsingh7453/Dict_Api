from django.db import router
from django.urls import URLPattern,include,path
from rest_framework import routers, urlpatterns
from .views import dict_view

router=routers.DefaultRouter()
router.register('dict',dict_view)


urlpatterns=[
    path('',include(router.urls))
]