import sqlite3
from flask import Flask, render_template, request
from werkzeug.exceptions import abort
import requests
import json

app = Flask(__name__)

url = "https://api.meraki.com/api/v1/"


headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-Cisco-Meraki-API-Key': ''
}
def getOrganizations(): 
      response = requests.request('GET', url + '/organizations', headers=headers)
      return response.json()

def storesbyorganization(organization):
      response = requests.request("GET", url + 'organizations/'+organization+'/networks', headers=headers)
      return response.json()
      

def devicesinnetwork(id_network):
    response = requests.request('GET', url + 'networks/'+ id_network + '/devices', headers=headers)
    equipos = response.json()
    return equipos

def puertos(serial):
  response = requests.request('GET', url + 'devices/'+ serial +'/switch/ports', headers = headers)
  puertos = response.json()
  return puertos

  
@app.route('/')
def index():
    organizations = getOrganizations()
    return render_template('index.html', posts=organizations)


app.run(host='0.0.0.0', port=81)
