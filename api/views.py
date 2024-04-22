import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Person, Transaction
from .serializers import PersonSerializer, TransactionSerializer


class PersonListAndCreate(APIView):
    def get(self, request):
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonDetailAndUpdatePartial(APIView):
    def get(self, request, pk):
        try:
            person = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response({"message": "Usuário não encontrado!"}, status=status.HTTP_404_NOT_FOUND)
    
        serializer = PersonSerializer(person)

        return Response(serializer.data)
    
    # Deposit
    def patch(self, request, pk):
        person = Person.objects.get(pk=pk)
        person.balance += request.data.get("balance")
        serializer = PersonSerializer(person, data=person.__dict__, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionListAndCreate(APIView):
    def get(self, request):
        transaction = Transaction.objects.all()
        serializer = TransactionSerializer(transaction, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            req = requests.get('https://run.mocky.io/v3/5794d450-d2e2-4412-8131-73d0293ac1cc').json()
            if req['message'] == "Autorizado":
                Transaction.update_balance(request.data)
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

