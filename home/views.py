from django.views.generic import TemplateView
from home.models import Settings


class HomeView(TemplateView):
    template_name = 'index.html'

    @staticmethod
    def get_page():
        return Settings.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = self.get_page()
        return context

