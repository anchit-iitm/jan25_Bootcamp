from flask import Flask, request

from models import db, test

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'

db.init_app(app)

with app.app_context():
    # db.drop_all()
    db.create_all()

@app.route('/helloworld')
def hello_world():
    return {"msg":'Hello, World!'}

@app.route('/firstApi', methods=['POST', 'GET', 'PUT', 'DELETE'])
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


if __name__ == '__main__':
    app.run(debug=True)