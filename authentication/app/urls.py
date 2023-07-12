from django.urls import path
from app import views

urlpatterns=[
    path('',views.BookLists.as_view(),name="book-list"),
    path('create',views.BookCreate.as_view(),name="create"),
    path('<int:pk>',views.BookDetail.as_view(),name="book-detail"),
]