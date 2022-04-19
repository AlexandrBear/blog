from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_posts),
    path('<str:pk>/', views.get_detail_post),
    path('<str:pk>/<str:lvl>/', views.get_lvl_comment),
]
