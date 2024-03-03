from .models import Settings


def page(*args, **kwargs):
    if _ := Settings.objects.first():
        return {'page': _}
