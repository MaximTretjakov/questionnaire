from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth.views import LoginView, LogoutView
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    re_path(r'^$', views.dashboard, name='dashboard'),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
]
