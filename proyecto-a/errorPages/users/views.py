from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth.decorators import login_required
import json
from .message import message
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})
def logout_view(request):
    logout(request)
    message_obj = message(
        "info", 
        "Se ha cerrado la sesión exitosamente",
        200, 
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8MIbugIhZBykSmQcR0QPcfnPUBOZQ6bm35w&s"  # Imagen
    )
    message_json = json.dumps(message_obj.to_dict())
    return render(request, "login.html", {"message": message_json})
@login_required
def home_view(request):
    return render(request, 'home.html')