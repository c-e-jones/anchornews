from . import views
from django.urls import path

urlpatterns = [
    path('',
    views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.article, name='article'),
    path('<slug:slug>/edit_comment/<int:comment:id>'),
    path()
]