from .models import Category


def categories(request):
    if categories := Category.objects.all():
        return {'categories': categories}
    return {'categories': None}