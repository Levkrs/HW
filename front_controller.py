def secret_front(request):
    request['secret'] = 'some secret key'


def user_name(request):
    request['username'] = 'USER NAME '


fronts = [secret_front, user_name]