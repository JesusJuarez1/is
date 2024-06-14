from django.urls import include, path
from minuta import views

urlpatterns = [
    path('', views.ConsultaMinutas.as_view(),name="consulta_minutas"),
    path('agregar/', views.agregar_minuta,name="agregar_minuta"),
    path('eliminar/<int:id>',views.eliminar_minuta, name='eliminar_minuta'),
    path('editar/<int:id>',views.editar_minuta, name='editar_minuta'),
    path('generar_pdf_minuta/<int:id>',views.generar_pdf_minuta, name='generar_pdf_minuta'),
]
