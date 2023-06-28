from core.models import User
from core.schemas import UserSchema
from flask import jsonify


class UserGateway():
    def add_user(self, name, phone_number, email, address):
        user = User.create(name=name, phone_number=phone_number, email=email, address=address)
        return {"id": user.id}
    
    def get_all_users(self):
        all_users = User.select()
        data = UserSchema().dump(all_users, many=True)
        return data