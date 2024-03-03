from django.views.generic import TemplateView, FormView
from django.urls import reverse
from django.contrib import messages
from home.models import Settings
from product.models import Product
from .forms import ContactForm


class HomeView(TemplateView):
    template_name = 'index.html'

    @staticmethod
    def get_page():
        return Settings.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # soru işareti random
        context['product_slider'] = Product.objects.order_by('?')[:4]
        context['trending_products'] = Product.objects.order_by('?')

        return context


class AboutView(TemplateView):
    template_name = 'aboutus.html'


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.ip = 'test'
            form.save()
            messages.success(request, 'Saved successfully!')
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('contact_page')

