from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user-activity', views.ActivityView.as_view()),
    path('activity', views.ActivityUserView.as_view()),
]