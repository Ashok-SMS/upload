from django.conf.urls import url,include
from formvalid.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('std', views.StudentView)
urlpatterns = [
    url('',include(router.urls))
]