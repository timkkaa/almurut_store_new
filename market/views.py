from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'

class PublicationDetailView(TemplateView):
    template_name = 'product-detail.html'


class PublicationListView(TemplateView):
    template_name = 'product-list.html'

    def get_context_data(self, **kwargs):
        context(


        )


class FaqView(TemplateView):
    template_name = 'faq.html'

class ErrorView(TemplateView):
    template_name = '404.html'

class FavoritesView(TemplateView):
    template_name = 'favorites.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class RegisterView(TemplateView):
    template_name = 'register.html'


class ShoppingView(TemplateView):
    template_name = 'shopping.html'

