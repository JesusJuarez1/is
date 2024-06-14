from django.core.exceptions import PermissionDenied
from usuario.models import UserTipo

def user_is_type(tipo):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                user_tipo = UserTipo.objects.filter(caseiuser=request.user).first()
                if user_tipo and user_tipo.tipoUser == tipo:
                    return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return _wrapped_view
    return decorator
