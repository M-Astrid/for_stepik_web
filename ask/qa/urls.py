from django.conf.urls import url

from . import views

app_name = 'qa_app'

urlpatterns = [
    url(r'^$', views.test, name='test'),
]