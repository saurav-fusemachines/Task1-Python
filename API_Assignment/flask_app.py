
import json
import re
from urllib import response
from xmlrpc.client import METHOD_NOT_FOUND
from flask import Flask, jsonify, request
  
# creating a Flask app
app = Flask(__name__)

#ROOT  
@app.route('/', methods = ['GET','POST','DELETE'])
def home():
    try:
     if(request.method == 'GET'):    
        with open('cart_data.json', 'r') as openfile:
            json_object = json.load(openfile)
        for i in json_object['carts']:
            return jsonify({'data': json_object})
    
    #  if  request.method == 'POST':
    #     return jsonify({'data':"STR"})

    except FileNotFoundError:
        return({
            'Status': 404,
            'error':'Resource error'
        })

#TOTAL EXPENDITURE
@app.route('/api/totalexp/<int:userId>',methods = ['GET'])
def totalexpenditure(userId):
    if(request.method == 'GET'):
        with open('cart_data.json','r') as openfile:
            json_object = json.load(openfile)
        for item in json_object['carts']: 
            if item['userId']==userId:
                 return jsonify({
                    'statusCode':200,
                    'userId':userId,
                    'total expenditure':item['total'],
                 })
            else:
                return jsonify({'status':'404',
                'message':'userId not found'})      
    openfile.close()

#DELETING RECORDS
@app.route('/api/del_rec/<int:id>',methods = ['DELETE'])
def deleterecord(id):
    f= open('cart_data.json','r')
    json_object = json.loads(f.read())
    f.close()
    try:
        for item in range(len(json_object['carts'])):
            try:
                if(json_object['carts'][items]['id']==id):
                    items = json_object['carts'][item]
                    del json_object['carts'][item]
            except:
                pass
        with open ('carts.json','w') as e:
            e.write(json.dumps(json_object))
        return f'<p>Successfully deleted folllowing item</p><pre>{json.dumps(items,indent=4)}</pre>'
    
    except:
        return jsonify({"error": "Item not found"})

    # try:
    #  if(request.method=='DELETE'): 
    #     with open('cart_data.json','r') as openfile:
    #         json_object = json.load(openfile)
    #     new_records =[]
    #     i = 0 
    #     for item in json_object['carts']:
    #           if item['id']==id:
    #                 i = 1
    #                 continue                 
    #           else:
    #             new_records.append(item)

    #     if i == 0:
    #         return  jsonify({'status':'404',
    #           'data':json_object,
    #              'message':'Id not found'})       
    #     else:
    #         return jsonify({'status':'200',
    #         "datas":new_records,
    #             'message':'success'}) 

    # except FileNotFoundError:
    #      return jsonify({"error":"Data resource not found"})

    # except METHOD_NOT_FOUND:
    #     return{"error":"request not found"}

@app.route('/api/insert', methods = ['POST'])
def insert_cart():
    try:
     if request.method == 'POST':  
        body = request.get_json()  
        with open('cart_data.json', 'r') as openfile:
            json_object = json.load(openfile)
        
        json_object['carts'].append(body)
        with open('cart_data.json','w') as insert_data:
            json.dump(json_object,insert_data)

        return jsonify({
            '':200,
            'amessage': 'New item added successfully',
            'item':body
        })   


    except FileNotFoundError:
        return({
            'Status': 404,
            'error':'Resource error'
        })
     

#Update the value
@app.route('/api/update/<int:id>',methods =['PUT'])
def update(id):
    if request.method == 'PUT':
        with open('cart_data.json','r') as openfile:
            json_object = json.load(openfile)
        
        for item in json_object['carts']:
            if item['id'] == id:
                # product_list = []
                # product_list = item['products']
                    
                for dict in item['products']:
                     for dict in item['products']:
                         dict["discountPercentage"] = int(dict["discountPercentage"])
                        #  return jsonify({"a":new_discountPercent})
                    # print(int(dict["discountPercentage"]))
                    
        with open ('cart_data.json','w') as e:
            e.write(json.dumps(json_object))
        return jsonify({"status":"success"})   


# Returns total number of products,total cost and status
@app.route('/api/getdata', methods = ['GET'])
def getdata():
    if request.method == 'GET':
        with open('cart_data.json',"r") as openfile:
            json_object = json.load(openfile)
        response = {}
        for item in json_object['carts']:
            response[item['id']]={
                         "total products":len(item['products']),
                         "total cost": item['total'],
                         "id":item['id']
                         }
        
        if len(response)>0 :
            return jsonify({"status":"Success",
                    "response":response })
        else:
            return jsonify({'status':404})             
           
    

    

if __name__ == '__main__':
    app.run(debug=True)
       