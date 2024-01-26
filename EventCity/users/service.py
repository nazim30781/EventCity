from .models import Profile


def create_profile(data, city):
    profile = Profile(user=data, city=city)
    profile.save()