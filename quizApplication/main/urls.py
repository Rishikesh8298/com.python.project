from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^quiz/(?P<word>.*)/$', views.quiz, name='quiz'),
    url(r'^result/(?P<word>.*)/$', views.result, name='result'),
    url(r'^panel/$', views.panel, name='panel'),
    url(r'^login/$', views.mylogin, name='mylogin'),
    url(r'^logout/$', views.mylogout, name='mylogout'),
    url(r'^panel/setting/$', views.site_setting, name='site_setting'),
    url(r'^panel/about/setting/$', views.about_setting, name='about_setting'),
    url(r'^panel/change/password/$', views.change_password, name='change_password'),
    url(r'^register/$', views.myregister, name='myregister'),
    url(r'^user/panel/$', views.user_panel, name='user_panel'),
]
