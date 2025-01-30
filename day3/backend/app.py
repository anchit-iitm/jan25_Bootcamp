from flask import Flask, request
from flask_security import Security, auth_required, roles_accepted

from flask_restful import Api
from flask_cors import CORS

from models import db, test, user_datastore
from config import Config, localdev

app = Flask(__name__)
app.config.from_object(localdev)
# import config
# app.config.from_object(config)

db.init_app(app)
Security(app, user_datastore)\

CORS(app)

api = Api(app)
from routes import first_restful
api.add_resource(first_restful, '/test1')

@app.route('/helloworld')
def hello_world():
    return {"msg":'Hello, World!'}

@app.route('/firstApi', methods=['POST', 'GET', 'PUT', 'DELETE'])
@auth_required('token')
@roles_accepted('manager')
def test1():
    if request.method == 'POST':
        if request.get_json(): # if request.form
            # var1 = request.get_json()['formKey'] # request.form['formKey']
            data = request.get_json()
            print(data)
            new_data = test(name=data['name'], age=data['age'])
            db.session.add(new_data)
            db.session.commit()
            return {"data": f'template print, {new_data.name}!'}
        return {"data": 'no data!'}
    
    if request.method == 'GET':
        data = test.query.first()
        if data:
            return {"data": data.name}
        return {"msg": 'This is a test API'}
    
    if request.method == 'PUT':
        data = request.get_json()
        update_data = test.query.filter_by(id=data['id']).first()
        update_data.name = data['name']
        update_data.age = data['age']
        db.session.commit()
        return {"msg": 'Data updated', "name": f'{update_data.name}', "age": f'{update_data.age}'}
    
    if request.method == 'DELETE':
        data = request.get_json()
        delete_data = test.query.filter_by(id=data['id']).first()
        db.session.delete(delete_data)
        db.session.commit()
        return {"msg": 'Data deleted', "name": f'{delete_data.name}', "age": f'{delete_data.age}'}

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = user_datastore.find_user(email=data['email'])
    if user:
        if user.password == data['password']:
            return {"msg": 'Login successful', "email": f'{user.email}', "authToken": user.get_auth_token()}, 202
        return {"msg": 'Invalid password'}, 417
    return {"msg": 'User not found'}, 404

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    user = user_datastore.find_user(email=data['email'])
    if not user:
        new_user = user_datastore.create_user(email=data['email'], password=data['password'])
        if data['role'] == 1:
            user_datastore.add_role_to_user(new_user, 'manager')
        if data['role'] == 2:
            user_datastore.add_role_to_user(new_user, 'customer')
        db.session.commit()
        return {"msg": 'User created', "email": f'{new_user.email}', "role": f'{new_user.roles[0].name}'}, 201
    return {"msg": 'User found, use a different email'}, 409

if __name__ == '__main__':
    app.run()