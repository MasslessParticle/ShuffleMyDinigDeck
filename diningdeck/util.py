from django.contrib.auth.models import User

def create_user(first_name, last_name, username, password):
    if len(User.objects.filter(username=username)) != 0:
        return False

    user = User.objects.create_user(username, email="", password=password)

    user.first_name = first_name
    user.last_name = last_name
    user.save()

    return True
