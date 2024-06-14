from django.urls import include, path
from Titulacion import views

urlpatterns = [
    path('', views.mostrar_titulacion,name="mostrar_titulacion"),
   
]
