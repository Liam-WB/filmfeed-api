from django.urls import path
from contact import views

urlpatterns = [
    path('contact/', views.ContactUsList.as_view()),
    path('contact/<int:pk>/', views.ContactUsDetail.as_view()),
]
