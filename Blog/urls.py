from django.urls import path
from . import views


urlpatterns = [
    path('addBlog/', views.addblog, name='addblog'),
    path('liBlog/', views.liblogs, name='liblogs'),
    path('csv/', views.csv, name='csv'),
    path('pdf/', views.pdf, name='pdf'),
    path('viewblog/', views.viewblog, name='viewblog'),
]

