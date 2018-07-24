from flask import Flask, render_template,request
from light_switch import LightSwitch
from threading import Thread
from pymongo import MongoClient
from numpy import array

app = Flask(__name__)
nn = NeuralNetwork()
client = MongoClient() 
db = client['data']
collection = db['all']

@app.route('/save')
def light_on():
    collection.insert(request.args) 

@app.route('/train')
def train():
    inputs=[]
    outputs=[]
    for data in collection.find():
        distance = data['distance']
        light = data['light']
        switch = data['switch']
        inputs.append([distance,light]
        outputs.append([switch])
    # TODO in new thread!
    nn.train(inputs,outputs,10000)   

@app.route('weights')
def getweights():
    pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
