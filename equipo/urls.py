from django.urls import path
from .views import equipo, equipo_base, equipo_base_delete, equipo_base_registrar, equipo_base_actualizar, \
                    equipo_delete, equipo_registrar, equipo_actualizar


urlpatterns = [
    path('', equipo, name='equipo'),
    path('delete/<int:id>/', equipo_delete, name='equipo_delete'),
    path('registrar/', equipo_registrar, name='equipo_registrar'),
    path('actualizar/<int:id>/', equipo_actualizar, name='equipo_actualizar'),

    path('base/', equipo_base, name='equipo_base'),
    path('base/delete/<int:id>/', equipo_base_delete, name='equipo_base_delete'),
    path('base/registrar/', equipo_base_registrar, name='equipo_base_registrar'),
    path('base/actualizar/<int:id>/', equipo_base_actualizar, name='equipo_base_actualizar'),
]
