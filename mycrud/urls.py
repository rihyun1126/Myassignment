from django.urls import path
from . import views

urlpatterns = [

    path('', views.read, name = "home"),
    path('newblog/', views.create, name = "newblog"),
    path('update/<int:pk>', views.update, name = "update"),
    path('delete/<int:pk>', views.delete, name = "delete"),
    path('detail/<int:blog_id>', views.detail, name = "detail"),
    path('detail/<int:pk>/update/', views.comment_update, name = "comment_update"),
    path('detail/<int:pk>/delete/', views.comment_delete, name = "comment_delete"),
]

    