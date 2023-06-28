class AddUserUsecase():
    def __init__(self, add_user_gateway):
        self.add_user_gateway = add_user_gateway
        
    def add_user(self, name=None, phone_number=None, email=None, address=None):
        if name is None or (phone_number is None and email is None) or address is None:
            return {"errors": ["NOT_PROVIDED"]}
        
        return self.add_user_gateway.add_user(name=name, phone_number=phone_number, email=email, address=address)
