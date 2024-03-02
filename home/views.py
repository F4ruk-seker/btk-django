from django.views.generic import TemplateView
from home.models import Settings
from product.models import Product


class HomeView(TemplateView):
    template_name = 'index.html'

    @staticmethod
    def get_page():
        return Settings.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = self.get_page()
        # soru işareti random
        context['product_slider'] = Product.objects.order_by('?')[:4]

        return context


class AboutView(TemplateView):
    template_name = 'aboutus.html'

    @staticmethod
    def get_page():
        return Settings.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = self.get_page()
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'

    @staticmethod
    def get_page():
        return Settings.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = self.get_page()
        return context
