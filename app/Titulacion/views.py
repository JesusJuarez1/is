from django.shortcuts import render

def mostrar_titulacion(request):
    return render(request, 'mostrar_info_titulacion.html')
