class GetAllUsersUsecase():
    def __init__(self, user_gateway):
        self.user_gateway = user_gateway

    def __call__(self):
        return self.user_gateway.get_all_users()