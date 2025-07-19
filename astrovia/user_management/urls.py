from django.urls import path
from .views import SignUpView, PhoneLoginView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', PhoneLoginView.as_view(), name='login'),
]
