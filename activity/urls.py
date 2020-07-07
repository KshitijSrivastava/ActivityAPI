from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path(r'^api-auth/', include('rest_framework.urls')),
    path('activity', views.ActivityUserView.as_view()),
]