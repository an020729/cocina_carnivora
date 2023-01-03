from django.urls import path
from .views import UserEditView, PwdChangeView, UserEditExtendedView
from django.contrib.auth import views as auth_views
from . import views

app_name = 'useraccount'
urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login_doggy, name='login'),
    path('password', PwdChangeView.as_view(template_name='registration/password.html'),name='password'),
    path('pwdsuccess', views.pwdsuccess, name='pwdsuccess'),
    path('<int:pk>', views.assign_role, name='assign_role'),
    path('logout',views.logout_doggy,name='logout'),
    path('editpro', UserEditView.as_view(), name='editpro'),

    path('password', PwdChangeView.as_view(template_name='registration/password.html'), name='password'),
    path('editprofile/<int:pk>/', UserEditExtendedView.as_view(), name='editprofile'), 
   
]

