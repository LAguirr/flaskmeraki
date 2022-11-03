import sqlite3
from flask import Flask, render_template, request, redirect,flash, url_for
from werkzeug.exceptions import abort
import requests
import json

app = Flask(__name__)

url = "https://api.meraki.com/api/v1/"

headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'X-Cisco-Meraki-API-Key': '',
}

def getOrganizations(apikey):
  
      headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-Cisco-Meraki-API-Key': apikey,
    }
      response = requests.request('GET', url + '/organizations', headers=headers)
      return response.json()

def networksbyorganization(organization):
      response = requests.request("GET", url + 'organizations/'+organization+'/networks', headers=headers)
      return response.json()
      

def devicesinnetwork(id_network):
    response = requests.request('GET', url + 'networks/'+ id_network + '/devices', headers=headers)
    equipos = response.json()
    return equipos

def ports(serial):
  response = requests.request('GET', url + 'devices/'+ serial +'/switch/ports', headers = headers)
  puertos = response.json()
  return puertos


@app.route('/',methods=["GET", "POST"])
def index():
    if request.method == 'POST':
      apikey = request.form['apikey']
      if apikey:
        headers['X-Cisco-Meraki-API-Key'] = apikey

        return redirect(url_for('organizations',apikey = apikey))
    return render_template('index.html')

@app.route('/organizations/<apikey>')
def organizations(apikey): 

  organizations = getOrganizations(apikey)
  return render_template('organizations.html',posts=organizations)

@app.route('/networks/<id_organization>')
def networks(id_organization):

  networks = networksbyorganization(id_organization)
  return render_template('networks.html', posts=networks)

@app.route('/devices/<id_network>')
def devices(id_network): 
  devices = devicesinnetwork(id_network)
  return render_template('devices.html', posts = devices)

@app.route('/switch/<serial>')
def switch(serial):
  switchports = ports(serial)
  return render_template('switch.html',posts = switchports)

app.run(host='0.0.0.0', port=81)
