from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('product-list/', views.showAll, name = 'product-list'),
    path('product-detail/<int:pk>', views.viewproduct, name = 'product-detail'),
    path('product-create/', views.createproduct, name = 'product-create'),
    path('product-update/<int:pk>', views.updateproduct, name = 'product-update'),
    path('product-delete/<int:pk>', views.deleteproduct, name = 'product-delete')
]