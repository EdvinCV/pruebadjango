from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pub, name='listar_pub'),
    path('post/<int:pk>/', views.detalle_pub, name='detalle_pub'),
    path('pub/nueva', views.nueva_pub, name='nueva_pub'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
