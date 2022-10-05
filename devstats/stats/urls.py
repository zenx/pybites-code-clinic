# django imports
from django.urls import path, include
# project imports
from stats import views


urlpatterns = [
    path('', views.developer_list, name='developer_list'),
    path('<str:username>', views.developer_detail, name='developer_detail'),
]
