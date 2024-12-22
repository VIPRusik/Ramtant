from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from users.models import Usr

def chat_list(request):
    return render(request, 'chat_list.html')

@login_required
def chat_direct(request, username):
    try:
        user = Usr.objects.get(username=username)
    except Usr.DoesNotExist:
        user = None
    
    if not user:
        return render(request, 'error.html')  # Ошибка, если пользователь не найден

    return render(request, 'direct.html', {'username': username})