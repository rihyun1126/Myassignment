from django.urls import path
from . import views
from .views import comment_delete, comment_update

urlpatterns = [
    path('', views.first, name = "home"),
    path('mycrud/', views.read, name = "showblog"),
    path('newblog/', views.create, name = "newblog"),
    path('update/<int:pk>', views.update, name = "update"),
    path('delete/<int:pk>', views.delete, name = "delete"),
    path('detail/<int:blog_id>', views.detail, name = "detail"),
    path('detail/update/<int:comment_id>/', comment_update, name = "comment_update"),
    path('detail/delete/<int:comment_id>/', comment_delete, name = "comment_delete"),
]

    