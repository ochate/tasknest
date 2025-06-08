from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')    # 後で作るログイン画面へ
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})


