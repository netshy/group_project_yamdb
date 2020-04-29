from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
import uuid
from .serializers import UserEmailSerializer, ConfirmationCodeSerializer, UserSerializer, UserInfoSerializer
from .models import User
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from rest_framework_simplejwt.tokens import AccessToken
from .permissions import AdminPermission
from rest_framework.views import APIView



@api_view(['POST'])
@authentication_classes([])
def send_confirmation_code(request):
    print(permission_classes)
    username = request.data.get('username')
    serializer = UserEmailSerializer(data=request.data)
    email = request.data.get('email')
    if serializer.is_valid():
        if username is not None:
            user = User.objects.filter(username=username) | User.objects.filter(email=email)
            if not user == 0:
                User.objects.create_user(username=username, email=email)
            else:
                return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
        confirmation_code = uuid.uuid3(uuid.NAMESPACE_DNS, email)

        send_mail(
            'Код подтверждения',
            f'Ваш код подтверждения: {confirmation_code}',
            'admin@admin.com',
            [email],
            fail_silently=False
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([])
def get_user_token(request):
    serializer = ConfirmationCodeSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.data.get('email')
        confirmation_code = serializer.data.get('confirmation_code')
        user = get_object_or_404(User, email=email)
        if str(uuid.uuid3(uuid.NAMESPACE_DNS, email)) == confirmation_code:
            token = AccessToken.for_user(user)

            return Response({f'token: {token}'}, status=status.HTTP_200_OK)
        return Response({'confirmation_code' : 'Неверный код подтверждения'},
                        status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    lookup_field = 'username'
    serializer_class = UserSerializer
    permission_classes = [AdminPermission]


class UserInfoViewSet(viewsets.ModelViewSet):
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)


class UserInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        print('REQ DATA', request.user)
        queryset = User.objects.get(username=request.user.username)
        serializer = UserInfoSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        user = User.objects.get(username=request.user.username)
        serializer = UserInfoSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)