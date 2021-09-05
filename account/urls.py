from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.contrib import admin

app_name = 'accounts'

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('delete_confirm', TemplateView.as_view(template_name='registration/delete_confirm.html'), name='delete-confirmation'),
    path('delete_complete', views.DeleteView.as_view(), name='delete-complete'),
]

admin.site.site_header = 'Yes&Home'
admin.site.site_title = 'Yes&Home'
admin.site.index_title = 'Yes&Home 管理ページ'
admin.site.site_urls= '/admin'