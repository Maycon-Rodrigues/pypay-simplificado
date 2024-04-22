from django.urls import path

from .views import PersonListAndCreate, PersonDetailAndUpdatePartial, TransactionListAndCreate

urlpatterns = [
    #person_route
    path("v1/persons", PersonListAndCreate.as_view(), name="person_list_and_post"),
    path("v1/person/<int:pk>", PersonDetailAndUpdatePartial.as_view(), name="person_detail"),
    path("v1/person/<int:pk>/deposit", PersonDetailAndUpdatePartial.as_view(), name="deposit"),

    #transaction_route
    path("v1/transactions", TransactionListAndCreate.as_view(), name="transaction_get_or_post"),
]
