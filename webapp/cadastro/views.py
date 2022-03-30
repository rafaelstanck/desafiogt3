from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Cadastro


class CadastroListView(ListView):
    model = Cadastro


class CadastroCreate(CreateView):
    model = Cadastro
    fields = ['nome', 'idade', 'observacao']
    template_name = 'cadastro/novo.html'
    success_url = reverse_lazy('cadastro:list')
