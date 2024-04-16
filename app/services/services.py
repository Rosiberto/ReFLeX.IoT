from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import uuid, requests, json
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


bp = Blueprint('serv', __name__, url_prefix='/serv')

url = "http://agentjson:4041/iot/services"

headers = {
          "fiware-service":"reflexiot",
          "fiware-servicepath":"/",
          "Content-Type":"application/json"
        }


@bp.route('/#', methods=['GET'])
def service():

    services = all()
    #print("s\n", services)
    return render_template('./services/service.html', services = services)


@bp.route('/#', methods=['POST'])
def create():
    if request.method == 'POST':
        entity_type = request.form['entity_type']
        resource    = request.form['resource']
        apikey      = uuid.uuid4().hex
       
        service = {}
        service['type']     = entity_type
        service['resource'] = "/" + "".join( resource )
        service['apikey']   = apikey

        #print('s-> ', service)
  
        message = {}
        message['services'] = []
        message['services'].append(service)

        #print('m-> ', message)

        error = None

        if not entity_type:
            error = 'Entity Type is required.'
        elif not resource:
            error = 'Resource is required.'
        
        if error is None:
            try:
                service_registration = requests.post(url,
                    headers  = headers,
                    json     = message,
                    verify   = False
                )
            except Exception as e:
                log.debug("Can't register service: {}".format(e))
                return  redirect(url_for("serv.service"))
                    
                flash(error)
                raise e
                
           # print("\n\n"+service_registration.text+"\n\n")
               
    return redirect(url_for("serv.service")) #render_template('./services/service.html')


def all():
    try:
        response = requests.get(url,
                headers  = headers,
                verify   = False
                )
            
        j = json.loads(response.text)
      
        return j
    except Exception as e:
        log.debug("Can't list service: {}".format(e))
        return  redirect(url_for("serv.service"))
                    
        flash(error)
        raise e
    

@bp.route('/remove/<key>', methods=['GET'])
def delete(key):

    #print(key)
    r = key.split("_")

    apikey     = r[0]
    resource   = r[1]
    resource   = resource.replace("-","/")
    #print(apikey)

    payload = "/?resource="+ resource +"&apikey="+ apikey
    #print(payload)


    if request.method == 'GET':     
       
        try:
            response = requests.delete(url+payload,
                                    headers  = headers,
                                    verify   = False
                    )
            print(response)

            return redirect(url_for("serv.service"))
        
        except Exception as e:
            log.debug("Can't list service: {}".format(e))
            return  redirect(url_for("serv.service"))
                    
            flash(error)
            raise e
