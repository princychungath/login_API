from django.urls import path
from app import views

urlpatterns=[
    path('',views.BookLists.as_view(),name="book-list"),
    path('create',views.BookCreate.as_view(),name="create"),
    path('update/<int:pk>',views.BookUpdate.as_view(),name="update"),
    path('delete/<int:pk>',views.BookDestroy.as_view(),name="destroy"),
    path('retrieve/<int:pk>',views.BookDetail.as_view(),name="retrieve"),
]