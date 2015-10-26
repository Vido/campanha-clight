# Para criar o ambiente:

Instalar o Python3 (3.4 ou 3.5):
* https://www.python.org/downloads/mac-osx/

Dentro do projeto `campanha-clight` ou num diretorio acima, criar o virtualenv para instalar as libs do projeto:

```
pyvenv env34

Comando para ativar o virtual env, toda vez que rodar o projeto a env tem que estar ativa. (o nome da env aparece no começo da linha no terminal)
source env/bin/activate
```

Com o virtualenv ativado, instale os pacotes do arquivo requirements.txt

```
pip install -r requirements.txt
```
dentro da pasta do projeto você encontra o script de manage do django "manage.py"
Para migrar a base de dados:

```
python manage.py migrate

```

# Para rodar o sistema
Antes de começar a trabalhar, certifique que o virtualenv está ativado.
Para levantar o servidor basta, rodar o `runserver` passando o ip externo da maquina e a porta

```
python manage.py runserver 127.0.0.1:8000

```
