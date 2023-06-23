from functools import wraps
from django.shortcuts import redirect

def permiso_requerido(permisos):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.tipo_permisos in permisos:
                return view_func(request, *args, **kwargs)
            else:
                # Redirigir a la página de acceso denegado o mostrar un mensaje de error
                return redirect('access_denied')
        return wrapper
    return decorator
