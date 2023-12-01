from functools import wraps
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def groups_required(groups):
    def decorator(view_func):
        @wraps(view_func)
        def check_groups(request, *args, **kwargs):
            if any(request.user.groups.filter(name=group).exists() for group in groups):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("Acesso negado. Você não tem permissão para acessar esta página.")

        return check_groups

    return decorator
