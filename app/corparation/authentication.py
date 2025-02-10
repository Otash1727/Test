from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Organazation

class OrganizationTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')

        if not token:
            token = request.GET.get('token')  # Support ?token= in URL

        if not token:
            raise AuthenticationFailed("Missing token")

        if token.startswith("Token "):
            token = token[6:]

        print(f"Received token: {token}")  # Debugging

        try:
            organization = Organazation.objects.get(token=token)
            print(f"Authenticated organization: {organization.title}")  # Debugging

            # Add `is_authenticated` dynamically
            organization.is_authenticated = True  # This makes DRF treat it as an authenticated user
            return (organization, None)

        except Organazation.DoesNotExist:
            raise AuthenticationFailed("Invalid Token")
