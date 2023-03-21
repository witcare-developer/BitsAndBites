django-admin startproject core .

python manage.py runserver

django-admin startapp cafeteria

python manage.py migrate

python manage.py makemigrations

python manage.py createsuperuser

senha criada: 1234

python manage.py shell


2 - Comando para gerar ambiente virtual:
    python -m venv <pasta-desejada>

3 - Para rodar o ambiente virtual
    Linux, Mac ...
    source <pasta-desejada>/bin/activate

    Windows
    <pasta-desejada>/Scripts/Acivate

4 - Configurar o Django para o ip da máquina local
    Vá na pasta core->settings.py e, dentro do código, altere a variável:
    ALLOWED_HOSTS = ['ip da sua máquina', 'localhost']
    Exemplo:
    ALLOWED_HOSTS = ['192.168.0.126', 'localhost']
    Assim a aplicação será liberada para própria máquina - localhost - e para qualquer um que quiser entrar na rede interna.

5 - Para saber qual ip interno da máquina:
    Em Windows, abrir o cmd e digitar ipconfig:
    
    Aparecerá algo assim....
    Endereço IPv6 Temporário. . . . . . . . : 2804:14c:110:a53c:ad2d:d3d7:60cd:c3a9   
    Endereço IPv6 de link local . . . . . . . . : fe80::f3d3:7ea9:6527:71b5%8
    Endereço IPv4. . . . . . . .  . . . . . . . : 192.168.0.126
    Máscara de Sub-rede . . . . . . . . . . . . : 255.255.255.0

    O ip é Endereço IPv4.

6 - Configurar o porta serial da impressora Bematch MP-4200
    A impressora já vem com Drive serial, quando conectar a impressora, basta procurar no seu sistema a porta 'COMX' relativo a impressora.

    Feito isso vá no arquivo views.py e na variável:
    SERIAL_PORT = "COM4" coloque a COMX correspondente. 

7 - por fim rodar o comando do Django:
    python manage.py runserver 0.0.0.0:80

    Onde o argumento 0.0.0.0:80 diz para o servidor django que qualquer dispositivo da rede pode acessar a aplicação. O 80 depois do dois pontos, o número é a porta da rede. O 80 é a porta padrão da internet mas pode ser outras portas também.
