import uuid

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, filters
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken

from .models import User, Categories, Review, Comments
from .permissions import AdminPermission, CategoriesPermission
from .serializers import (
    UserEmailSerializer,
    ConfirmationCodeSerializer,
    UserSerializer,
    UserInfoSerializer,
    CategoriesSerializer,
    ReviewsSerializer,
    CommentsSerializer,
)


@api_view(['POST'])
@authentication_classes([])
def send_confirmation_code(request):
    serializer = UserEmailSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.data['email']
        user_is_exist = User.objects.filter(email=email).exists()
        if not user_is_exist:
            # username same as email
            User.objects.create_user(username=email, email=email)
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
        email = serializer.data['email']
        confirmation_code = serializer.data['confirmation_code']
        user = get_object_or_404(User, email=email)
        # generate code to check with confirmation code
        code = str(uuid.uuid3(uuid.NAMESPACE_DNS, email))
        if code == confirmation_code:
            token = AccessToken.for_user(user)
            return Response({f'token: {token}'}, status=status.HTTP_200_OK)
        return Response({'confirmation_code': 'Неверный код подтверждения'},
                        status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    lookup_field = 'username'
    serializer_class = UserSerializer
    permission_classes = [AdminPermission]


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    lookup_field = 'slug'
    serializer_class = CategoriesSerializer
    permission_classes = [CategoriesPermission]

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class UserInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
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


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer