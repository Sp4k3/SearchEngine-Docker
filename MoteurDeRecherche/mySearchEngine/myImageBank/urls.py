from django.urls import path
from myImageBank import views

urlpatterns = [
    path('myImageBank/', views.ImageList.as_view()),
    path('myImageBank/random/', views.RandomImage.as_view()),
    path('myImageBank/inverted/', views.KeywordList.as_view()),
    path('myImageBank/<int:pk>/', views.Image.as_view()),
    path('myImageBank/<str:name>/', views.ImagesByName.as_view()),
    path('myImageBankRegex/<str:name>/', views.ImagesByRegex.as_view()),
]
