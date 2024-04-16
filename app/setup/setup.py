from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, Response, jsonify
)

from werkzeug.exceptions import abort

import requests
import docker

client = docker.from_env()
#client = docker.DockerClient(base_url='unix://var/run/docker.sock')

bp = Blueprint('set', __name__, url_prefix='/set')


@bp.route('/#',  methods=['GET'])
def setup():

    retorno = find()  
    
    listContainers = []
    listContainers = client.containers.list(all=True)
        
    return render_template('./setup/setup.html', containers=listContainers, retorno = retorno)
    

@bp.route('/pause/<id>', methods=['GET'])
def pause(id):

    if request.method == 'GET':     
        client.containers.get(id).pause()

    return redirect(url_for('set.setup'))


@bp.route('/remove/<id>', methods=['GET'])
def remove(id):

    if request.method == 'GET':     
        client.containers.get(id).remove()

    return redirect(url_for('set.setup'))


@bp.route('/unpause/<id>', methods=['GET'])
def unpause(id):

    if request.method == 'GET':     
        client.containers.get(id).unpause()

    return redirect(url_for('set.setup'))


@bp.route('/start/<id>', methods=['GET'])
def start(id):

    if request.method == 'GET':     
        client.containers.get(id).start()

    return redirect(url_for('set.setup'))


@bp.route('/stop/<id>', methods=['GET'])
def stop(id):

    if request.method == 'GET':     
        client.containers.get(id).stop()

    return redirect(url_for('set.setup'))



#Subscription
headersGETDELETE = {
          "fiware-service":"reflexiot",
          "fiware-servicepath":"/"          
        }

headers = {
          "fiware-service":"reflexiot",
          "fiware-servicepath":"/",
          "Content-Type":"application/json"
        }

subscription = {
              "description": "Notify Cygnus of all context changes",
              "subject": {
               "entities": [
                 {
                   "idPattern": ".*"
                 }
               ]
              },
              "notification": {
                "http": {
                  "url": "http://cygnus:5050/notify"
                },
              "attrsFormat": "legacy"
              },
                "throttling": 5
            }


@bp.route('/#', methods=['GET','POST'])
def activate():
    cygnus_registration = requests.post('http://orion:1026/v2/subscriptions',
                          headers=headers,
                          json=subscription,
                          verify=False
                        )
    #print("\n\n"+cygnus_registration.text+"\n\n")
    #print(cygnus_registration.headers['Location'])
    #return cygnus_registration.text
    return redirect(url_for("set.setup"))


def find():
    try:
        response = requests.get('http://orion:1026/v2/subscriptions',
                          headers=headersGETDELETE,                          
                          verify=False
                        ) 
       
    except requests.exceptions.ConnectionError as e:
        return False
  
    #print("=> "+ response.text )
    if response.text == "[]" or None:
        return False
  
    return True



