from flask_restful import Resource
from flask import request, make_response, jsonify
from flask_security import auth_required, roles_accepted

from models import db, test, category, product


class first_restful(Resource):
    @auth_required('token')
    @roles_accepted('manager')
    def post(self):
        if request.get_json(): # if request.form
            # var1 = request.get_json()['formKey'] # request.form['formKey']
            data = request.get_json()
            print(data)
            new_data = test(name=data['name'], age=data['age'])
            db.session.add(new_data)
            db.session.commit()
            return {"data": f'template print, {new_data.name}!'}
        return make_response(jsonify({"data": 'no data!'}), 404)
    
    @auth_required('token')
    @roles_accepted('manager')    
    def get(self):
        data = test.query.first()
        if data:
            return {"data": data.name}
        return {"msg": 'This is a test API'}

    @auth_required('token')
    @roles_accepted('manager')    
    def put(self):
        data = request.get_json()
        update_data = test.query.filter_by(id=data['id']).first()
        update_data.name = data['name']
        update_data.age = data['age']
        db.session.commit()
        return {"msg": 'Data updated', "name": f'{update_data.name}', "age": f'{update_data.age}'}

    @auth_required('token')
    @roles_accepted('manager')   
    def delete(self):
        data = request.get_json()
        delete_data = test.query.filter_by(id=data['id']).first()
        db.session.delete(delete_data)
        db.session.commit()
        return {"msg": 'Data deleted', "name": f'{delete_data.name}', "age": f'{delete_data.age}'}
    

class crud_category(Resource):
    @auth_required('token')
    @roles_accepted('admin')
    def post(self):
        if request.get_json():
            data = request.get_json()
            new_data = category(name=data['name'], description=data['description'])
            db.session.add(new_data)
            db.session.commit()
            return make_response(jsonify({"msg": 'Data added', "name": f'{new_data.name}', "description": f'{new_data.description}'}), 201)
        return make_response(jsonify({"msg": 'No data!'}), 404)
    
    @auth_required('token')    
    @roles_accepted('admin', 'manager', 'customer')
    def get(self):
        data = category.query.all()
        if data:
            return make_response(jsonify({"data": [{"name": i.name, "description": i.description, "id": i.id} for i in data]}), 200)
        return make_response(jsonify({"msg": 'No data!'}), 404)
    
    @auth_required('token')
    @roles_accepted('admin')    
    def put(self):
        data = request.get_json()
        update_data = category.query.filter_by(id=data['id']).first()
        update_data.name = data['name']
        update_data.description = data['description']
        db.session.commit()
        return make_response(jsonify({"msg": 'Data updated', "name": f'{update_data.name}', "description": f'{update_data.description}'}), 200)
    
    @auth_required('token')
    @roles_accepted('admin')    
    def delete(self):
        data = request.get_json()
        delete_data = category.query.filter_by(id=data['id']).first()
        db.session.delete(delete_data)
        db.session.commit()
        return make_response(jsonify({"msg": 'Data deleted', "name": f'{delete_data.name}', "description": f'{delete_data.description}'}), 200)
    
class crud_products(Resource):
    @auth_required('token')
    @roles_accepted('admin', 'manager')
    def post(self):
        if request.get_json():
            data = request.get_json()
            new_data = product(name=data['name'], description=data['description'], price=data['price'], category_id=data['category_id'])
            db.session.add(new_data)
            db.session.commit()
            return make_response(jsonify({"msg": 'Data added', "name": f'{new_data.name}', "description": f'{new_data.description}', "price": f'{new_data.price}', "category_id": f'{new_data.category_id}'}), 201)
        return make_response(jsonify({"msg": 'No data!'}), 404)
    
    @auth_required('token')
    @roles_accepted('admin', 'manager', 'customer')    
    def get(self):
        data = product.query.all()
        if data:
            return make_response(jsonify({"data": [i.name for i in data]}), 200)
        return make_response(jsonify({"msg": 'No data!'}), 404)
    
    @auth_required('token')
    @roles_accepted('admin', 'manager')    
    def put(self):
        data = request.get_json()
        update_data = product.query.filter_by(id=data['id']).first()
        update_data.name = data['name']
        update_data.description = data['description']
        update_data.price = data['price']
        update_data.category_id = data['category_id']
        db.session.commit()
        return make_response(jsonify({"msg": 'Data updated', "name": f'{update_data.name}', "description": f'{update_data.description}', "price": f'{update_data.price}', "category_id": f'{update_data.category_id}'}), 200)
    
    @auth_required('token')
    @roles_accepted('admin', 'manager')    
    def delete(self):
        data = request.get_json()
        delete_data = product.query.filter_by(id=data['id']).first()
        db.session.delete(delete_data)
        db.session.commit()
        return make_response(jsonify({"msg": 'Data deleted', "name": f'{delete_data.name}', "description": f'{delete_data.description}', "price": f'{delete_data.price}', "category_id": f'{delete_data.category_id}'}), 200)