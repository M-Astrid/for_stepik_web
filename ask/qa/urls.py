from django.conf.urls import url

from . import views

app_name = 'qa'

urlpatterns = [
    url(r'^popular/', views.test, name='test'),
]