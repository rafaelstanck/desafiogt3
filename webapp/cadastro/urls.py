from django.urls import path
from . import views
from .views import CadastroCreate

app_name = 'cadastro'

urlpatterns = [
    path('', views.CadastroListView.as_view(), name='list'),
    path('novo/', CadastroCreate.as_view(), name='cadastrar'),
]
