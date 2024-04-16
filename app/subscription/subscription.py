from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import json, requests

bp = Blueprint('sig', __name__, url_prefix='/sig')


@bp.route('/subscription', methods=['GET'])
def subscription():
    
    retorno = find()

    return render_template('./subscriptions/subscription.html', retorno = retorno)



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


@bp.route('/activate', methods=['GET','POST'])
def activate():
    cygnus_registration = requests.post('http://orion:1026/v2/subscriptions',
                          headers=headers,
                          json=subscription,
                          verify=False
                        )
    #print("\n\n"+cygnus_registration.text+"\n\n")
    #print(cygnus_registration.headers['Location'])
    #return cygnus_registration.text
    return redirect(url_for("sig.subscription"))

def find():
  response = requests.get('http://orion:1026/v2/subscriptions',
                          headers=headersGETDELETE,                          
                          verify=False
                        ) 
  #print("=> "+ response.text )

  if response.text == "[]":
     return False
  
  return True
  