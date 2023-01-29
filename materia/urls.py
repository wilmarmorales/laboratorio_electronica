from django.urls import path
from .views import materia, materia_delete, materia_registrar, materia_actualizar, \
                    estudiante, estudiante_delete, estudiante_registrar, estudiante_actualizar
                    



urlpatterns = [
    path('', materia, name='materia'),
    path('delete/<int:id>/', materia_delete, name='materia_delete'),
    path('registrar/', materia_registrar, name='materia_registrar'),
    path('actualizar/<int:id>/', materia_actualizar, name='materia_actualizar'),

    path('estudiante/<url>/', estudiante, name='estudiante'),
    path('estudiante/delete/<int:id>/<int:materia_id>/', estudiante_delete, name='estudiante_delete'),
    path('estudiante/registrar/<int:id>', estudiante_registrar, name='estudiante_registrar'),
    path('estudiante/actualizar/<int:id>/<int:materia_id>/', estudiante_actualizar, name='estudiante_actualizar'),
]