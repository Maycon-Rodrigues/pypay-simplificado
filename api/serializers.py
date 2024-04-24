import requests
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
        
        # Simular uma solicitação ao serviço autorizador externo
        url = "https://run.mocky.io/v3/5794d450-d2e2-4412-8131-73d0293ac1cc"
        response = requests.get(url)
        
        # Verificar se a resposta do serviço autorizador é bem-sucedida
        if response.status_code == 200:
            data = response.json()
            # Verificar o status da autorização
            if data.get('message') == "Autorizado":
                # A transação é autorizada
                return attrs
            else:
                # A transação não é autorizada
                raise serializers.ValidationError({'message': 'Transação não autorizada pelo serviço externo.'})
        else:
            # Lidar com erros de conexão ou respostas inesperadas
            raise serializers.ValidationError({'message': 'Erro ao consultar o serviço autorizador externo.'})


        