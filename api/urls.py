from django.urls import path

from . import views

urlpatterns = [
    #person_route
    path("v1/persons", views.person, name="person_get_or_post"),
    path("v1/person/<int:pk>", views.person_detail, name="person_detail"),
    path("v1/person/<int:pk>/deposit", views.deposit, name="deposit"),

    #transaction_route
    path("v1/transactions", views.transaction, name="transaction_get_or_post"),
]
