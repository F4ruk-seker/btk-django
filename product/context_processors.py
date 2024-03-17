from .models import Category


def categories(request):
    if _ := Category.objects.all():
        return {'categories': _}
    return {'categories': None}

