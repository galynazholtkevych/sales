from django.conf.urls import url, include
from django.contrib.auth.views import logout

from rest_framework.routers import DefaultRouter

from .views import RegisterView, LoginView, APILoginView


app_name = 'customauth'

router = DefaultRouter(trailing_slash=True)
# router.register('login', APILoginView.as_view(), base_name='login')

urlpatterns = [
   url(r'^login/$', LoginView.as_view(), name='login'),
   url(r'^register/$', RegisterView.as_view(), name='register'),
   url(r'^logout/$', logout, name='logout'),
   url(r'^api-login/$', APILoginView.as_view(), name='api-login')
]

