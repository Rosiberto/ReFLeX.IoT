from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import logging, json, os, requests
from pathlib import Path


bp = Blueprint('dev', __name__, url_prefix='/dev')


url = "http://agentjson:4041/iot/devices"

headers = {
          "fiware-service":"reflexiot",
          "fiware-servicepath":"/",
          "Content-Type":"application/json"
        }

smart_data_model = "./smart_data_model/"
extension = ['json']


@bp.route('/#', methods=['GET'])
def device():
    list_models = load()

    #print ('x -> ', list_models)
    return render_template('./devices/device.html', list_models = list_models)


@bp.route('/##')
def devices():   
    list_devices = all()

    #print("\n",list_devices, "\n")

    return render_template('./devices/devices.html', list_devices = list_devices)


def load():
    
    files = os.listdir( smart_data_model )

    list_models = {}
    list_models['model'] = files

    return list_models


@bp.route('/create', methods=['POST'])
def save():

    if request.method == 'POST':
        device_id   = request.form['device_id']
        entity_name = request.form['entity_name']
        entity_type = request.form['entity_type']
        model_id    = request.form['model_id']

    files =  os.listdir( smart_data_model ) 
    
    #logging.debug(f"Reading file '{smart_data_model}'")
    
    with open(smart_data_model + model_id) as json_device_file:
        payload = json.load( json_device_file )
           
    device_schema_json_str = json.dumps( payload )
      
    device_schema = device_schema_json_str.replace('[DEVICE_ID]', str(device_id)) \
                                          .replace('[ENTITY_ID]', str(entity_name)) \
                                          .replace('[ENTITY_TYPE]', str(entity_type))

    error = None

    if not device_id:
        error = 'Id device is required.'        
    if not entity_name:
        error = 'Entity Name is required.'
    if not entity_type:
        error = 'Entity Type is required.'
    elif not model_id:
        error = 'Model is required.'
        
    if error is None:
        try:
            response = requests.post(url,
                headers  = headers,
                data     = device_schema,
                verify   = False                
            )
          
        except Exception as e:
            logging.debug("Can't register device: {}".format(e))
            
            return  redirect(url_for("dev.device"))
                    
            flash(error)
            raise e
        
    return redirect(url_for("dev.device"))      


def all():
    try:
        response = requests.get(url,
                headers  = headers,
                verify   = False
                )
            
        j = json.loads(response.text)
      
        return j
    except Exception as e:
        logging.debug("Can't list device: {}".format(e))
        return  redirect(url_for("dev.device"))
                    
        flash(error)
        raise e
    

@bp.route('/remove/<key>', methods=['GET'])
def delete(key):

    #print("\nkey ",key)
    
    payload = "/"+ key
    #print("\nP-> ",payload)

    if request.method == 'GET':     
        try:
            response = requests.delete(url+payload,
                                    headers  = headers,
                                    verify   = False
                        )
            
        #    print("\n", response)

            return redirect(url_for("dev.devices"))
        
        except Exception as e:
            logging.debug("Can't list device: {}".format(e))
            return  redirect(url_for("dev.devices"))
                    
            flash(error)
            raise e
