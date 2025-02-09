from models import db, user_datastore
from app import app

with app.app_context():
    # db.drop_all()
    db.create_all()

    user_datastore.find_or_create_role(name='admin')
    user_datastore.find_or_create_role(name='manager')
    user_datastore.find_or_create_role(name='customer')

    admin_user = user_datastore.find_user(id=1)
    if not admin_user:
        new_admin = user_datastore.create_user(email='admin@abc.com', password='admin')
        user_datastore.add_role_to_user(new_admin, 'admin')
    manager = user_datastore.find_user(email='m1@abc.com')
    if not manager:
        new_manager = user_datastore.create_user(email='m1@abc.com', password='m1')
        user_datastore.add_role_to_user(new_manager, 'manager')
    customer = user_datastore.find_user(email='c1@abc.com')
    if not customer:
        new_manager = user_datastore.create_user(email='c1@abc.com', password='c1', roles=['customer'])
    db.session.commit()


    db.session.commit()
