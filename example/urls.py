from django.conf.urls import url
from example import views

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^signup/', views.signup,name='signup'),
]
