from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import FormView, RedirectView, TemplateView
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from .forms import LoginForm, RegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import UserProfile
from order.models import Order, OrderProduct
from product.models import Comment
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse('home_page')

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if user := authenticate(username=username, password=password):
                if user.is_active:
                    login(request, user)
            else:
                raise self.form_invalid(form)

        return super(LoginView, self).post(request, *args, **kwargs)


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'

    def get_success_url(self):
        return reverse('home_page')

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        super(RegisterView, self).post(request, *args, **kwargs)


class LogoutView(RedirectView):

    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')


class PanelView(TemplateView):
    template_name = 'main_panel.html'

    def get_context_data(self, **kwargs):
        context = super(PanelView, self).get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.get(user=self.request.user)
        return context


class ProfileView(TemplateView, LoginRequiredMixin):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.get(user=self.request.user)
        context['user_update_form'] = UserUpdateForm(instance=self.request.user)
        context['profile_update_form'] = ProfileUpdateForm(instance=self.request.user.userprofile)
        return context

    def post(self, request, *args, **kwargs):
        user_update_form = UserUpdateForm(request.POST, instance=self.request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_update_form.is_valid():
            user_update_form.save()
        if profile_update_form.is_valid():
            profile_update_form.save()

        return HttpResponseRedirect(reverse('profile'))


class UserPasswordChangeView(PasswordChangeView):
    # LoginRequiredMixin
    ...


class UserCommentsView(LoginRequiredMixin, TemplateView):
    template_name = 'user_comments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(user=self.request.user)
        return context


class CommentDeleteView(LoginRequiredMixin, RegisterView):

    def post(self, request, *args, **kwargs):
        comment_id = request.POST.get('comment_id')
        if comment := Comment.objects.filter(id=comment_id).first():
            comment.delete()
        return HttpResponseRedirect(reverse('comments'))


class UserOrderView(LoginRequiredMixin, TemplateView):
    template_name = 'user_order_products.html'

    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data(**kwargs)
        context['order_products'] = OrderProduct.objects.filter(user=self.request.user).order_by('-id')
        print(context)
        return context


class UserOrderDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'user_order_detail.html'

    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data(**kwargs)

        order = Order.objects.filter(user=self.request.user, id=kwargs.get('pk')).first()
        context['order_product'] = OrderProduct.objects.filter(order=order)
        context['order'] = order
        return context
