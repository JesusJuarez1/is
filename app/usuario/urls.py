from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.lista_usuarios, name='usuarios'), # temporal
    path('registro/', views.registrar_usuario, name='registrar'),
    path('editar/<int:pk>', views.editar_usuario, name='editar'),
    path('eliminar/<int:pk>', views.eliminar_usuario, name='eliminar'),
    path('info/<int:pk>', views.obtener_usuario, name='info'),
    path('enviar_correo/', views.enviar_correo_usuario, name='enviar_correo'),
    path('subir/', views.subir_documento, name='subir_documento'),
    path('documento/eliminar/<int:pk>/', views.eliminar_documento, name='eliminar_documento'),
    path('lista_documentos/', views.lista_documentos, name='lista_documentos'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
    path('evaluaciones/', views.evaluacion_template, name='evaluaciones'), # URL TEMPORAL
    path('historial_alumno/', views.historial_alumno, name='historial_alumno'), # URL TEMPORAL
    path('actividades/', views.actividades, name='actividades'), # URL TEMPORAL
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/<int:pk>/', views.perfil_usuario, name='perfil_usuario'),
    path('solicitar_cambio_actividades/', views.solicitar_cambio_actividades, name='solicitar_cambio_actividades'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

