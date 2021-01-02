from main import app, db, Admin

admin_list = [
    {'id_': 123, 'username':'admin123', 'pswd':'@dmin123'}
]

for i in admin_list:
    insert_admin = Admin(id_=i['id_'], username=i['username'], pswd=i['pswd'])
    db.session.add(insert_admin)
    db.session.commit()
