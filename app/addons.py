from django.http import JsonResponse
from hashlib import sha256


def tryexception(view_func):
    def wrapper(*args, **kwargs):
        try:
            return view_func(*args, **kwargs)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return wrapper
