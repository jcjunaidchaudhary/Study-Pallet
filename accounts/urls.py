from django.urls import path
from .controllers import (
    dashboard,
    home,
    register,
    signin,
    signout
)
urlpatterns = [
    path('', home.start, name="home" ),
    path('dashboard', dashboard.dashboard, name="dashboard" ),
    path('signup', register.register, name="signup"),
    path('signin', signin.signin, name="signin"),
    path('signout', signout.signout, name="signout"),
]