from django.urls import path
# from .views import SignUpView
from . import views
from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

]
