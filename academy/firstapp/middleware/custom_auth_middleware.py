

from firstapp.models import User

class CustomUser:
    def __init__(self, user):
        self.id = user.id
        self.username = user.username
        self.is_authenticated = True

class AnonymousUser:
    is_authenticated = False
    username = 'Гость'

def custom_auth_middleware(get_response):
    def middleware(request):
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                request.user = CustomUser(user)
            except User.DoesNotExist:
                request.user = AnonymousUser()
        else:
            request.user = AnonymousUser()

        return get_response(request)
    return middleware
