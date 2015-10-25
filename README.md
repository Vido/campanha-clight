# Para criar o ambiente:

Instalar o Python3 (3.4 ou 3.5):
* https://www.python.org/downloads/mac-osx/

Dentro do projeto `campanha-clight`, criar o virtualenv:

```
pyvenv env
source env/bin/activate
```

Com o virtualenv ativado, instale os pacotes do arquivo requirements.txt

```
pip install -r requirements.txt
```

Para migrar a base de dados:

```
python manage.py migrate

```

# Para rodar o sistema
Antes de começar a trabalhar, certifique que o virtualenv está ativado.
Para levantar o servidor basta, rodar o `runserver` passando o ip externo da maquina e a porta

```
python manage.py runserver 192.168.0.130:8000

```
