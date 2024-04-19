from rest_framework import serializers

from .models import Person, Transaction


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'person_type', 'document', 'name', 'last_name', 
                  'email', 'balance']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('payer').person_type == 'S':
            raise serializers.ValidationError({'message': 'Lojistas não podem realizar transferências.'})
        elif attrs.get('payer') == attrs.get('payee'):
            raise serializers.ValidationError({'message': 'O pagador e o beneficiário não podem ser a mesma pessoa.'})
        elif attrs.get('payer').balance < attrs.get('amount'):
            raise serializers.ValidationError({'message': 'Saldo insuficiente pare realizar está trnsação.'})

        return attrs
        