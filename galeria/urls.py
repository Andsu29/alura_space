from django.urls import path
from galeria.views import index, imagem, mais

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('mais/', mais, name='mais'),
]