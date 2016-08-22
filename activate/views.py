from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django.db.models import Q
from registration.models import HubreeUser


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def activate_user(request):
    """
    Activate a new user.
    """
    if request.method == 'POST':
        email = request.data['email']
        results = HubreeUser.objects.filter(Q(email=email))
        if results:
            for rec in results:
                rec.verificationstatus = True
                rec.save()
            return Response({'email':email,
                             'message':'User Activated'}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"message":"No user for this email"}, status=status.HTTP_400_BAD_REQUEST)
