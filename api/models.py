from django.db import models
from django.core.exceptions import ValidationError
from rest_framework import serializers


class Person(models.Model):
    PERSON_TYPE = (
        ('C', 'COMMON'),
        ('S', 'SHOPKEEPER'),
    )

    person_type = models.CharField(max_length=1, choices=PERSON_TYPE, default='C')
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document = models.CharField(max_length=100, unique=True, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    
    def __str__(self):
        return self.name
    
    
    def full_name(self):
        return self.name + " " + self.last_name


class Transaction(models.Model):
    payer = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='payer')
    payee = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='payee')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

   
    def __str__(self):
        return str(self.id)

    @staticmethod
    def update_balance(data):
        payer = Person.objects.get(pk=data['payer'])
        payee = Person.objects.get(pk=data['payee'])
        payer.balance -= data['amount']
        payee.balance += data['amount']
        payer.save()
        payee.save()
