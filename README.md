
# PyPay Simplificado

API de realizações bancarias, como crição de conta, deposito e transferencia.


## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/Maycon-Rodrigues/pypay-simplificado.git
```

Entre no diretório do projeto

```bash
  cd pypay-simplificado
```

Crie um ambiente virtual e ative-o

```bash
  python -m venv venv
  source ./venv/bin/activate #(Linux/Mac)
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

Gerando as migrações

```bash
  python manage.py migrate
```

Inicie o servidor

```bash
  python manage.py runserver
```


## Licença

[MIT](https://choosealicense.com/licenses/mit/)

