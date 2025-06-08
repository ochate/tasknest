from django.contrib import admin
from django.urls import path, include

# プロジェクト全体のURL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('tasks/', include('tasks.urls')),
]
