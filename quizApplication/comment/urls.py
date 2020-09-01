from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^feedback/$", views.feedback, name="feedback"),
    url(r"^panel/comment/list/$", views.comment_list, name="comment_list"),
    
]