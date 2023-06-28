from core.models import User


class UserGateway():
    def add_user(self, name, phone_number, email, address):
        user = User.create(name=name, phone_number=phone_number, email=email, address=address)
        return {"id": user.id}