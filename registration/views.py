from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.db.models import Q
from .models import HubreeUser
from .serializers import HubreeUserSerializer

def home(request):
    return render(request,'home.html')

def register_form(request):
    return render(request, 'registration_form.html')


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def create_user(request):
    """
    Create a new user.
    """
    if request.method == 'GET':
        hubree_users = HubreeUser.objects.all()
        serializer = HubreeUserSerializer(hubree_users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HubreeUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = request.data['email']
            generate_email(email)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def register_user(request):
    """
    Create a new user.
    """
    if request.method == 'GET':
        hubree_users = HubreeUser.objects.all()
        serializer = HubreeUserSerializer(hubree_users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HubreeUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = request.data['email']
            generate_email(email)
            return render_to_response('confirmation.html')
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                
def generate_email(request,email):
    """ """
    send_mail('Welcome to Hubree', 'Welcome to Hubree, Real estate app, Plick below link to activate', 'hubreeh@gmail.com',
    [email], fail_silently=False)
    
