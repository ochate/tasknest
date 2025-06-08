from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views

# プロジェクト全体のURL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', accounts_views.home_view, name='home'),    # トップページ
    path('tasks/', include('tasks.urls')),
]
