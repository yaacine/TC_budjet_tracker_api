from django.contrib.auth.models import User
from .models import Tag, Transaction
from .filters import TransactionFilter
from .serializers import UserSerializer, TagSerializer, TransactionSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import viewsets
# from rest_framework.status import HTTP_401_UNAUTHORIZED
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.views import TokenObtainPairView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class HelloView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)



# class LoginView(TokenObtainPairView):
#     def post(self, request, *args, **kwargs):
#         if not request.user:
#             token = RefreshToken.for_user(request.user)
#             content = {'token': str(token.access_token), 'user': request.user}
#             return Response(content)
#         else:
#             return Response(status=HTTP_401_UNAUTHORIZED)


class UserRegistrationView(CreateAPIView):
    queryset = User.objects
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class CurrentUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        # if self.request.method != 'GET':
        #     self.permission_classes = (IsAdminUser,)

        return super(TagViewSet, self).get_permissions()


class TransactionViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = TransactionFilter
    search_fields = ['date', 'amount', 'type', 'tags__name']
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
