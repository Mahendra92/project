from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django.db.models import Q
from registration.models import HubreeUser

def login(request):
    return render(request,'login.html')


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def login_user(request):
    """
    Login a new user.
    """
    if request.method == 'POST':
        email = request.data['email']
        password = request.data['password']

        results = HubreeUser.objects.filter(Q(email=email) & Q(password=password))
        if results:
            for rec in results:
                verification_status = rec.verificationstatus
                if verification_status:
                    return Response({"message":"Logged in Successfully"}, status=status.HTTP_201_CREATED)
                else:
                    # return Response(
                       # {"message":"User not yet activated"}, status=status.HTTP_400_BAD_REQUEST)
                    return render(request, 'active.html')
 
        else:
            return Response(
                {"message":"Invalid Username/Password"}, status=status.HTTP_400_BAD_REQUEST)
