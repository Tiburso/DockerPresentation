from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/clients'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = [{'name': user.name, 'email': user.email} for user in users]
    return jsonify(result)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data['name']
    email = data['email']
    new_user = User(name, email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'})

if __name__ == '__main__':
    app.run(debug=True)
