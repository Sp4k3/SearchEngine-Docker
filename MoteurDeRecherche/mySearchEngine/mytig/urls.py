from django.urls import path
from mytig import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.RedirectionProductList.as_view(), name='projectRoot'),
    path('products/', views.RedirectionProductList.as_view(), name='mytigProducts'),
    path('product/<int:pk>/', views.RedirectionProductDetail.as_view()),

    path('onsaleproducts/', views.OnSaleList.as_view()),
    path('onsaleproduct/<int:pk>/', views.OnSaleDetail.as_view()),

    path('availableproducts/', views.AvailableList.as_view()),
    path('availableproduct/<int:pk>/', views.AvailableDetail.as_view()),

    path('product/<int:pk>/image/', views.ProductImageRandom.as_view()),
    path('product/<int:tigID>/image/<int:pk>/', views.ProductImage.as_view()),
]
