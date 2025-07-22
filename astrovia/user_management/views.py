from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import SignUpSerializer, PhoneLoginSerializer
from .models import UserProfile
from rest_framework.authtoken.models import Token
from testing_1 import chat_with_bot

class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "message": "User created",
                "token": token.key
            }, status=201)
        return Response(serializer.errors, status=400)
    def get(self, request):
        users = User.objects.all()
        return Response({"users": list(users)}, status=200)


class PhoneLoginView(APIView):
    def post(self, request):
        serializer = PhoneLoginSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone_number']
            try:
                user_profile = UserProfile.objects.get(phone_number=phone)
                user = user_profile.user
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    "message": "Login success",
                    "user_id": user.id,
                    "token": token.key
                })
            except UserProfile.DoesNotExist:
                return Response({"error": "Phone number not found"}, status=404)
        return Response(serializer.errors, status=400)



class ChatBotAPIView(APIView):
    def post(self, request, *args, **kwargs):
        message = request.data.get("message", "").strip()
        if not message:
            return Response({"error": "Message field is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        reply = chat_with_bot(message)
        return Response({"response": reply}, status=status.HTTP_200_OK)