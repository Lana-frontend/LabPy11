from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

from model.fix import Fix
from model.rating import Rating
from model.type import Type

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    rating = db.Column(db.String)
    fix = db.Column(db.String)
    producer = db.Column(db.String)
    type = db.Column(db.String)
    power = db.Column(db.String)

    def __init__(self, price, producer, rating, fix, power, type):
        self.price = price
        self.producer = producer
        self.rating = rating
        self.fix = fix
        self.power = power
        self.type = type

        def __str__(self):
            return ', '.join((f"{name} = {value}" for name, value in self.__dict__.items()))

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('price', 'producer', 'rating', 'fix', 'power', 'type')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/', methods=['GET'])
def index():
    return ''


# endpoint to create new user
@app.route("/users", methods=["POST"])
def add_user():
    price = request.json['price']
    producer = request.json['producer']
    rating = request.json['rating']
    fix = request.json['fix']
    power = request.json['power']
    type = request.json['type']

    new_user = User(price, producer, rating, fix, power, type)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)


# endpoint to show all users
@app.route("/users", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)


# endpoint to get user detail by id
@app.route("/users/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


# endpoint to update user
@app.route("/users/<id>", methods=["PUT"])
def user_update(id):

    user = User.query.get(id)
    user.price = request.json['price']
    user.producer = request.json['producer']
    user.rating = request.json['rating']
    user.fix = request.json['fix']
    user.power = request.json['power']
    user.type = request.json['type']

    db.session.commit()
    return user_schema.jsonify(user)


# endpoint to delete user
@app.route("/users/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)