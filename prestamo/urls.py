from django.urls import path
from .views import prestamos_list, prestamos_list_all, entrega, registrar

urlpatterns = [
    #path('materia/list/', MateriaList.as_view(), name='materia_list'),
    path('', prestamos_list, name='prestamo'),
    path('all/', prestamos_list_all, name='prestamo_all'),
    path('entrega/<int:id>/', entrega, name='entrega'),
    path('all/entrega/<int:id>/', entrega, name='entrega_all'),
    path('registrar/', registrar, name='registrar'),

]