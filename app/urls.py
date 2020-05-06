from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.PostIndex.as_view(), name='post_list'),
    path('/delete/<int:pk>', views.PostDelete.as_view(), name='post_delete'),   
]