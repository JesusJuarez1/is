from django.conf import settings
from django.core.mail import send_mail
from .models import CaseiUser

# Manda correo (Puede cambiar en caso de enviar un correo con html)
def enviar_correo(notificacion):
    subject = notificacion.get('asunto')
    message = notificacion.get('mensaje')
    from_email = settings.EMAIL_HOST_USER
    recipient_list = correo_usuario(notificacion.get('tipo_usuario'))
    
    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False
    )
    
    
# obtiene correos de usuario especificado por tipo
def correo_usuario(tipo_usuario):
    if( tipo_usuario == 'todos' ):
        correos = CaseiUser.objects.all().values_list('email', flat=True)
    else:
        correos = CaseiUser.objects.filter(usertipo__tipoUser=tipo_usuario).values_list('email', flat=True)
        
    return correos
