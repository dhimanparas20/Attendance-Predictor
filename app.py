from flask_restful import Resource, Api
from flask import render_template
from os import system
from flask import *

system("clear")

# The function that predicts.
def check(curr_lec,tot_lec):
  temp = curr_lec
  per=(curr_lec/tot_lec)*100
  perc =per
  if per >=75:
    print("\n--------| PERCENTAGE IN SAFE ZONE |--------\n")
    no = curr_lec-temp
    no,curr_lec,tot_lec = 0,0,0
    return no,curr_lec,tot_lec,perc
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
    print("\n--------------------------")
    print("Home Page loaded") 
    print("--------------------------\n")
    curr_lec = request.args.get('curr_lec')
    tot_lec = request.args.get('tot_lec')
    name = request.args.get('name')
    print(name,curr_lec,tot_lec)
    
    #For default page
    if curr_lec  == None or name == None:
      print("\n--------| None ASSIGNMNET |--------")
      curr_lec,tot_lec,name = 1,1,""

    tmp,v1,v2,perc = check(int(curr_lec),int(tot_lec))
    return make_response(render_template('index.html',temp=tmp,val1=v1,val2=v2,per=perc,name=name))
    
api.add_resource(Home, '/',methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True)    
