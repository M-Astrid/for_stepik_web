from django.conf.urls import url

from . import views

app_name = 'qa'

urlpatterns = [
    url(r'^$', views.main),
    url(r'^login/', views.login_view,
    url(r'^signup/', views.signup, name='signup'),
    url(r'^question/(?P<num>[0-9]+)/', views.question),
    url(r'^ask/', views.go_ask),
    url(r'^popular/', views.popular),
    url(r'^new/', views.main),
]