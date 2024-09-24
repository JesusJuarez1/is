from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.views import LoginView as DjangoLogoutView
from django.urls import reverse_lazy
from .forms import RegistrarUsuarioForm, DocumentoForm, LoginForm, NotificacionForm, SolicitudCambioActividadesForm
from .models import CaseiUser, UserTipo, Documento
from .functions import enviar_correo
from usuario.tools.decorators import user_is_type

# Create your views here.

# Crea un nuevo usuario
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El usuario ha sido registrado correctamente.')
            return redirect('usuarios')
    else:
        form = RegistrarUsuarioForm()
    return render(request, 'usuario/registrar_usuarios.html', {'form': form})

# Obtiene y muestra todos los usuarios
@login_required
@user_is_type('coordinador')
def lista_usuarios(request):
    usuarios = CaseiUser.objects.all()
    return render(request, 'usuario/lista_usuarios.html', {'usuarios': usuarios})

# Obtiene un usuario especifico por llave primaria
@login_required
def obtener_usuario(request, pk):
    usuario = get_object_or_404(CaseiUser, pk=pk)
    if usuario != request.user:  # Asegúrate de que solo accede a su propia información
        return HttpResponseForbidden("No tienes permiso para ver esta información.")
    try:
        tipo = UserTipo.objects.get(caseiuser=usuario)
    except UserTipo.DoesNotExist:
        tipo = None
    return render(request, 'usuario/info_usuario.html', {'usuario_cacei': usuario, 'tipo_cacei': tipo.tipoUser})


# Actualiza información de un usuario especifico por llave primaria
@login_required
@user_is_type('coordinador')  # Solo coordinadores pueden editar otros usuarios
def editar_usuario(request, pk):
    usuario = get_object_or_404(CaseiUser, pk=pk)
    if usuario != request.user:  # Si el usuario no es el mismo
        return HttpResponseForbidden("No tienes permiso para editar este perfil.")
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'El usuario ha sido actualizado correctamente.')
            return redirect('usuarios')
    else:
        form = RegistrarUsuarioForm(instance=usuario)
    return render(request, 'usuario/registrar_usuarios.html', {'form': form})


# Elimina un usuario especifico por llave primaria
@login_required
@user_is_type('coordinador')  # Solo coordinadores pueden eliminar usuarios
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(CaseiUser, pk=pk)
    if usuario == request.user:  # Prevenir que un usuario se elimine a sí mismo
        return HttpResponseForbidden("No puedes eliminar tu propia cuenta.")
    usuario.delete()
    messages.success(request, 'El usuario ha sido eliminado correctamente.')
    return redirect('usuarios')

#Manda al perfil al usuario (temporal) SI

# Manda correo a usuarios especificados (temporal)
@login_required
@user_is_type('coordinador')
def enviar_correo_usuario(request):
    if request.method == 'POST':
        form = NotificacionForm(request.POST)
        if form.is_valid():
            notificacion = {
                'asunto': form.cleaned_data['asunto'],
                'mensaje': form.cleaned_data['mensaje'],
                'tipo_usuario': form.cleaned_data['tipo_usuario']
            }
            enviar_correo(notificacion)
            messages.success(request, 'Se ha enviado notificación correctamente.')
            return redirect('usuarios')
    else:
        form = NotificacionForm()
    return render(request, 'usuario/enviar_correo_usuario.html', {'form': form})
#Perfil de usuario

@login_required
def perfil_usuario(request, pk):
    usuario = get_object_or_404(CaseiUser, pk=pk)
    if usuario != request.user:  # Solo permite ver su propio perfil
        return HttpResponseForbidden("No tienes acceso a este perfil.")
    # Continuar con la lógica original
    try:
        tipo = UserTipo.objects.get(caseiuser=usuario)
        es_coordinador = tipo.tipoUser == 'coordinador'
        es_tutor = tipo.tipoUser == 'tutor'
    except UserTipo.DoesNotExist:
        tipo = None
        es_coordinador = False
        es_tutor = False

    documentos = Documento.objects.first()

    return render(request, 'usuario/perfil_usuario.html', {
        'usuario': usuario,
        'tipo_cacei': tipo.tipoUser if tipo else "N/A",
        'ultimo_documento': documentos,
        'es_coordinador': es_coordinador,
        'es_tutor': es_tutor
    })



#Función para subir los documentos
@login_required
@user_is_type('coordinador')
def subir_documento(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Se les notifica a todos los tutores del nuevo contenido
            # agregado por el coordinador.
            notificacion = {
                'asunto': 'Nuevo plan de acción',
                'mensaje': f"El coordinador ha subido nuevo documento '{form.cleaned_data['nombre']}' como plan de acción a seguir para todos los tutores",
                'tipo_usuario': 'tutor',
            }
            enviar_correo(notificacion=notificacion)
            return redirect('confirmacion')
        else:
            print(form.errors)
    else:
        form = DocumentoForm()
    return render(request, 'usuario/subir_documento.html', {'form': form})

#Eliminar documentos
@login_required
@user_is_type('coordinador')
def eliminar_documento(request, pk):
    if request.method == 'POST':
        documento = get_object_or_404(Documento, pk=pk)
        documento.archivo.delete()
        documento.delete()
        return redirect('lista_documentos')
    else:
        return HttpResponse("No permitido", status=405)
    
#Enlistar y mostrar los documentos subidos
@login_required
@user_is_type('coordinador')
def lista_documentos(request):
    documentos = Documento.objects.all()
    return render(request, 'usuario/lista_documentos.html', {'documentos': documentos})

#Página de confirmación (temporal)
@login_required
def confirmacion(request):
    return render(request, 'usuario/confirmacion.html')

# Template de evaluaciones (temporal) Pendiente implementar
def evaluacion_template(request):
    return render(request,'usuario/evaluaciones.html')

#Template del historial de alumno (temporal) Pendinete implementar
def historial_alumno(request):
    return render(request,'usuario/historial_alumno.html')

#Template del historial de alumno (temporal) Pendinete implementar
def actividades(request):
    return render(request,'usuario/actividades.html')

#Funciones para el login y el logout de usuarios    
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('perfil_usuario', pk=user.pk)
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos')
    else:
        form = LoginForm()
    return render(request, 'usuario/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente")
    return redirect('login')

# Función para enviar correo de solicitud de cambio de actividades
def enviar_solicitud_actividades(asunto, mensaje, destinatario):
    try:
        send_mail(
            asunto,
            mensaje,
            settings.EMAIL_HOST_USER,
            [destinatario],
            fail_silently=False,
        )
        return True, None
    except Exception as e:
        return False, str(e)
    
# Vista para solicitar cambio de actividades
@login_required
@user_is_type('estudiante')
def solicitar_cambio_actividades(request):
    if request.method == 'POST':
        form = SolicitudCambioActividadesForm(request.POST)
        if form.is_valid():
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']
            estudiante = form.cleaned_data['estudiante']
            
            success, error_message = enviar_solicitud_actividades(asunto, mensaje, estudiante.email)
            if success:
                messages.success(request, 'La solicitud de cambio de actividades ha sido enviada.')
            else:
                messages.error(request, f'Ocurrió un error al enviar el correo: {error_message}')
    else:
        form = SolicitudCambioActividadesForm()
    
    return render(request, 'notificaciones/solicitar_cambio_actividades.html', {'form': form})
