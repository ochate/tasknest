from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# サインアップ（新規登録）画面
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')    # 後で作るログイン画面へ
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

# 仮トップページ表示用の関数
def home_view(request):
    print(f"ユーザー認証状態: {request.user.is_authenticated}")
    print(f"ユーザー名: {request.user.username if request.user.is_authenticated else '匿名'}")
    return render(request, 'home.html')