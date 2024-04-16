from flask import (
    Blueprint, g, render_template
)

import docker
client = docker.from_env()

from werkzeug.exceptions import abort


bp = Blueprint('pages', __name__)


@bp.route('/')
def logar():
    return render_template('./auth/login.html')

@bp.route('/#')
def index():    
    #print(cli.containers.get('mongo').stats(stream=False)['cpu_stats'])
    #print('---------------------------------------------')
    #print(cli.containers.get('mongo').stats(stream=False)['precpu_stats'])
   

    return render_template('./pages/index.html')


def metrics():
    #listContainers = []
    #listContainers = client.containers.list(all=True)

    for container in client.containers.list(all=True):
        stats = client.containers.get(container.id).stats(stream=False)
      
        UsageDelta = stats['cpu_stats']['cpu_usage']['total_usage'] - stats['precpu_stats']['cpu_usage']['total_usage']
        # from informations : UsageDelta = 25382985593 - 25382168431
        #print("\nUsageDelta -----> ", UsageDelta)

        SystemDelta = stats['cpu_stats']['system_cpu_usage'] - stats['precpu_stats']['system_cpu_usage']
        # from informations : SystemDelta = 75406420000000 - 75400410000000
        #print("SystemDelta -----> ", SystemDelta)
    
        len_cpu = len(stats['cpu_stats']['cpu_usage']['percpu_usage'])
        # from my informations : len_cpu = 2
        #print("len_cpu -----> ", len_cpu)

        percentage = (UsageDelta / SystemDelta) * len_cpu * 100
        # this is a little big because the result is : 0.02719341098169717
        #print("percentage -----> ", percentage)

        percent = round(percentage, 2)
        # now The output is 0.02 and thats the answer.
        #print("percent -----> ", percent)


    return None