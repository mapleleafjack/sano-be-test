from core.models import User
from core.schemas import UserSchema
from flask import jsonify


class UserGateway():
    def add_user(self, name, phone_number, email, address):
        if name is None or phone_number is None or email is None or address is None:
            return {"errors": ["NOT_PROVIDED"]}

        user = User.create(name=name, phone_number=phone_number, email=email, address=address)
        return {"id": user.id}
    
    def get_all_users(self):
        all_users = User.select()
        data = UserSchema().dump(all_users, many=True)
        return data
    
    def get_user_by_id(self, id):
        if id is None:
            return {"errors": ["NOT_PROVIDED"]}

        user = User.get_or_none(id=id)
        if user is None:
            return None
        return user