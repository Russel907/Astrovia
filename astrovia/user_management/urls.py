from django.urls import path
from .views import SignUpView, PhoneLoginView, ChatBotAPIView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', PhoneLoginView.as_view(), name='login'),
    path('api/chat/', ChatBotAPIView.as_view(), name='chatbot-api'),
]
