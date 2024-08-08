import sys
print("----",sys.path[0])
import requests
from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from User.userService import UserService
from User.userRepository import User
from flask import Blueprint

user_blue_print = Blueprint("user_blue_print", __name__)
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/test"
engine = create_engine(SQLALCHEMY_DATABASE_URL)


@user_blue_print.route("/user/<id>", methods=["GET"])
def get_user_by_id(id):
    userservice = UserService(engine)
    information = userservice.get_user_by_ID(ID=id)
    return jsonify(information)
@user_blue_print.route("/users", methods=["GET"])
def get_all_users():
    userservice = UserService(engine)
    information = userservice.get_all_users()
    print(information)
    return jsonify(information)
@user_blue_print.route("/user", methods=["POST"])
def create_user():
    Name = request.json.get("Name")
    Nationality = request.json.get("Nationality")

    user_serivce = UserService(engine)
    user_serivce.create_user(
        Name=Name,
        Nationality=Nationality,
    )
    return jsonify({"message": "user created successfully"}), 201
