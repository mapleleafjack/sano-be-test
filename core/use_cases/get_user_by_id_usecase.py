class GetUserByIdUseCase:
    def __init__(self, user_gateway):
        self.user_gateway = user_gateway

    def __call__(self, user_id):
        if user_id is None:
            return {"errors": ["NOT_PROVIDED"]}

        return self.user_gateway.get_user_by_id(user_id)
