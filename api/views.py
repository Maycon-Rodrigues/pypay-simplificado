from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from .models import Person, Transaction
from .serializers import PersonSerializer, TransactionSerializer


@api_view(["GET", "POST"])
def person(request):
    if request.method == "GET":
        serializer = PersonSerializer(Person.objects.all(), many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def person_detail(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response({"message": "Usuário não encontrado!"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = PersonSerializer(person)

    return Response(serializer.data)


@api_view(["PATCH"])
def deposit(request, pk):
    person = Person.objects.get(pk=pk)
    person.balance += request.data.get("balance")
    serializer = PersonSerializer(person, data=person.__dict__, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def transaction(request):
    transaction = Transaction.objects.all()
    if request.method == "GET":
        serializer = TransactionSerializer(transaction, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            req = requests.get('https://run.mocky.io/v3/5794d450-d2e2-4412-8131-73d0293ac1cc').json()
            if req['message'] == "Autorizado":
                Transaction.update_balance(request.data)
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)