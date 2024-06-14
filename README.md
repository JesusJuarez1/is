# Repositorio de proyecto CACEI

Instalación de docker y docker compose:

~~~
# Añadir al repositorio de linux la llave GPT de docker:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Añadir al repositorio de APT:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
#Instalación:
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo apt-get install docker-compose-plugin
~~~

Clonar el repo:
~~~
git clone https://github.com/DanteFX/cacei.git
~~~
 

Ingresar al repo:
~~~
cd cacei 
~~~

Inicialización y descarga de contenedores:
~~~
docker compose up -d
~~~

Ingresar al contenedor de la app:
~~~
docker compose exec app bash
~~~

Salir de la sesión:
~~~
exit
~~~

Apagar contenedot:
~~~
docker compose down
~~~
~~~
NO ES NECESARIO CORRER "python3 manage.py runserver 0:8000"
~~~

> CACEI TEAM
