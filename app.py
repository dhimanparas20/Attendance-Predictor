from flask_restful import Resource, Api
from flask import render_template
from os import system,path
from flask import *
import json,time
import requests

system("clear")

def check(curr_lec,tot_lec):
  temp = curr_lec
  per=(curr_lec/tot_lec)*100
  perc =per
  if per >=75:
    return curr_lec-temp,curr_lec,tot_lec,perc
  else:
    while per < 75 :
      curr_lec +=1
      tot_lec +=1
      per =  (curr_lec/tot_lec)*100
    return curr_lec-temp,curr_lec,tot_lec,perc

#staring web app
app = Flask(__name__)
api = Api(app)

class Home(Resource):
  def get(self):
    print("--------------------------")
    print("Home Page loaded") 
    curr_lec = request.args.get('curr_lec')
    tot_lec = request.args.get('tot_lec')
    print(curr_lec)
    print(tot_lec)
    if curr_lec  == None:
      curr_lec,tot_lec = 1,1 
    tmp,v1,v2,perc = check(int(curr_lec),int(tot_lec))
    if perc >=75:
      tmp,v1,v2 = 0,0,0
    
    return make_response(render_template('index.html',temp=tmp,val1=v1,val2=v2,per=perc))
    
api.add_resource(Home, '/',methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True)    