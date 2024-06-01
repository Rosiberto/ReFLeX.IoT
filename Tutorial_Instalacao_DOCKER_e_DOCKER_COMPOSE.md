### Este é um guia simplificado de como instalar o Docker e Docker Compose V2 em máquinas Linux.
### Disciplina: Apl.Cloud, IoT, Indústria 4.0 em Python
### Prof. Dr. Rosiberto Santos
### Ano 2024



#1. Instalar Docker e Docker Compose v2 no UBUNTU, copie e cole os comandos abaixo e os execute.

 sudo apt-get -y update
 sudo apt-get -y upgrade
 curl -fsSL https://get.docker.com -o get-docker.sh
 sudo sh get-docker.sh
 
 

#2. Para verificar se os dois foram instalados, execute os comandos abaixo.
 docker --version
 docker compose version
 
 
 
#3. Ative a permissão.
 sudo chmod 666 /var/run/docker.sock
 
 
 
#4. Pronto!!! Agora é hora de instalar o ReFLex.IoT.