from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from antisocial.api.models import User, NeighborHood, Business, Post, ContactInfo
from .serializers import UserSerializer, NeighborhoodSerializer, ContactInfoSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)

        return Response(
            {
                'token': token.key,
                'user': serializer.data,
                'created': created
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class ObtainAuthTokenAndUserDetails(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(ObtainAuthTokenAndUserDetails, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)

        return Response({
            'token': token.key,
            'user': {
                'id': user.id,
                'last_login': user.last_login,
                'is_superuser': user.is_superuser,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_staff': user.is_staff,
                'date_joined': user.date_joined,
                'email': user.email,
                'neighborhood': user.neighborhood,
            }
        })


class UserDetailsFromToken(RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        print(request.user)
        return Response(dict(
            user={
                'id': request.user.id,
                'last_login': request.user.last_login,
                'is_superuser': request.user.is_superuser,
                'username': request.user.username,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'is_staff': request.user.is_staff,
                'date_joined': request.user.date_joined,
                'email': request.user.email,
                'neighborhood': request.user.neighborhood,
            }
        ))


class NeighborHoodViewSet(viewsets.ModelViewSet):
    queryset = NeighborHood.objects.all()
    serializer_class = NeighborhoodSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request, *args, **kwargs):
        neighborhoods = NeighborHood.objects.all()
        serializer = NeighborhoodSerializer(neighborhoods, many=True)
        neighborhoods_expanded = []

        for neighborhood in serializer.data:
            admin = User.objects.get(id=dict(neighborhood)['admin'])
            user = User.objects.get(id=dict(neighborhood)['created_by'])
            neighborhoods_expanded.append({
                'id': dict(neighborhood)['id'],
                'name': dict(neighborhood)['name'],
                'location': dict(neighborhood)['location'],
                'members': len(User.objects.filter(neighborhood=dict(neighborhood)['id'])),
                'date_created': dict(neighborhood)['date_created'],
                'admin': {
                    'id': admin.id,
                    'last_login': admin.last_login,
                    'is_superuser': admin.is_superuser,
                    'username': admin.username,
                    'first_name': admin.first_name,
                    'last_name': admin.last_name,
                    'is_staff': admin.is_staff,
                    'date_joined': admin.date_joined,
                    'email': admin.email,
                    'neighborhood': admin.neighborhood,
                },
                'created_by': {
                    'id': user.id,
                    'last_login': user.last_login,
                    'is_superuser': user.is_superuser,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'is_staff': user.is_staff,
                    'date_joined': user.date_joined,
                    'email': user.email,
                    'neighborhood': user.neighborhood,
                }
            })

        return Response(neighborhoods_expanded)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = NeighborHood.objects.all()
        neighborhood = get_object_or_404(queryset, pk=pk)
        serializer = NeighborhoodSerializer(neighborhood)
        admin = User.objects.get(id=serializer.data['admin'])
        user = User.objects.get(id=serializer.data['created_by'])
        return Response({
            **serializer.data,
            'members': len(User.objects.filter(neighborhood=neighborhood.id)),
            'admin': {
                'id': admin.id,
                'last_login': admin.last_login,
                'is_superuser': admin.is_superuser,
                'username': admin.username,
                'first_name': admin.first_name,
                'last_name': admin.last_name,
                'is_staff': admin.is_staff,
                'date_joined': admin.date_joined,
                'email': admin.email,
                'neighborhood': admin.neighborhood,
            },
            'created_by': {
                'id': user.id,
                'last_login': user.last_login,
                'is_superuser': user.is_superuser,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_staff': user.is_staff,
                'date_joined': user.date_joined,
                'email': user.email,
                'neighborhood': user.neighborhood,
            }
        })


class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request, *args, **kwargs):
        contact_info = ContactInfo.objects.all()
        serializer = ContactInfoSerializer(contact_info, many=True)
        contact_info_expanded = []

        for contact_info_piece in serializer.data:
            user = User.objects.get(id=dict(contact_info_piece)['user'])
            contact_info_expanded.append({
                'id': dict(contact_info_piece)['id'],
                'facility': dict(contact_info_piece)['facility'],
                'phone_number': dict(contact_info_piece)['phone_number'],
                'phone_number_2': dict(contact_info_piece)['phone_number_2'] if 'phone_number_2' in dict(contact_info_piece) else None,
                'email': dict(contact_info_piece)['email'],
                'date_created': dict(contact_info_piece)['date_created'],
                'user': {
                    'id': user.id,
                    'last_login': user.last_login,
                    'is_superuser': user.is_superuser,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'is_staff': user.is_staff,
                    'date_joined': user.date_joined,
                    'email': user.email,
                },
            })

        return Response(contact_info_expanded)


class NeighborhoodContactInfoViewSet(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        queryset = ContactInfo.objects.filter(neighborhood=self.kwargs['id'])
        serializer = ContactInfoSerializer(queryset, many=True)
        return Response(serializer.data)
