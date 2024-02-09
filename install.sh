function full(){
	echo "downloading images, creating containers, starting containers"
	cd composes
	docker-compose -p reflexiot up -d --remove-orphans
}

function default(){
	cd composes/d
	docker-compose -p reflexiot up -d --remove-orphans
}

function basic(){
	cd composes/b
	docker-compose -p reflexiot up -d --remove-orphans
}

function dcp(){
	echo "Initializing the installation Docker and Docker Compose"
	sudo apt-get -y update
	sudo apt-get -y upgrade
	sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
	sudo add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
	sudo apt-get -y update
	sudo apt-get -y install docker-ce
	sudo systemctl status docker
	echo "Install Docker Compose"
	sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
	sudo chmod +x /usr/local/bin/docker-compose
	docker-compose --version
}


function CheckOptions () {
	if [ $1 = "create" ] && [ $2 = "-f" ]; then
		full
	elif [ $1 = "create" ] && [ $2 = "-d" ]; then
		default
	elif [ $1 = "create" ] && [ $2 = "-b" ]; then
		basic
	elif [ $1 = "start" ]; then
		echo "starting containers"
		docker-compose -p reflexiot start
	elif [ $1 = "stop" ]; then
		echo "stopping containers"
		docker-compose -p reflexiot stop
	elif [ $1 = "unpause" ]; then
		echo "unpausing containers"
		docker-compose -p reflexiot unpause
	elif [ $1 = "pause" ]; then
		echo "pausing containers"
		docker-compose -p reflexiot pause
	elif [ $1 = "remove" ] && [ $2 = "-c" ]; then
		echo "removing containers"
		docker-compose -p reflexiot down
	elif [ $1 = "remove" ] && [ $2 = "-all" ]; then
		echo "removing containers and images"
		docker-compose -p reflexiot down --rmi all
	elif [ $1 = "dc" ]; then
		dcp
	else
		echo -e "\n\n' $1 $2 ' Command not Found."
		echo -e "\nusage: commands [create|pause|unpause|stop|start|remove|dc]"      
		exit 1
	fi
}

echo -e "\n		Initializing the installation of ReFLeX.IoT Platform"
echo -e "This is a script created to help set up the ReFLeX.Io System Available commands:\n 
	
	create  -> creates and starts the system containers based on the docker-compose.yml file and of parameter past.

		usage: create [PARAMETER]		

		[PARAMETER] = "-f" (Full); "-d" (Default); "-b" (Basic);
		
	pause   -> pause the system containers (doesn't delete data).
	unpause\n
	stop    -> stop the system containers without removing.\n 
	start   -> start stopped system containers.\n
	remove  -> remove system containers and images.
		
		usage: remove [PARAMETER]		

		[PARAMETER] = "-c" (Containers); "-all" (Containers and Images);\n
	dc -> Install Docker and Docker Compose\n"
echo -n "Insert Command: "
read x;


CheckOptions $x