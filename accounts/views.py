from django.contrib.auth import logout, authenticate, login
from django.http import JsonResponse
from django.views import View
from django.middleware.csrf import get_token

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    """
    A view that handles user login.

    Methods:
    - post(self, request): Handle POST request for user login.
    """
    
    def post(self, request):
        """
        Handle POST request for user login.

        Parameters:
        - request (HttpRequest): The HTTP request object.

        Returns:
        - JsonResponse: JSON response indicating login status.
        """
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            csrf_token = get_token(request)
            return JsonResponse({
                "detail": "Successfully logged in.",
                "csrf_token": csrf_token,
            }, status=200)
        return JsonResponse({"detail": "Invalid credentials."}, status=400)



class LogoutView(View):
    """
    A view that handles user logout.

    Methods:
    - post(self, request): Handle POST request for user logout.
    """
    def post(self, request):
        """
        Handle POST request for user logout.

        Parameters:
        - request (HttpRequest): The HTTP request object.

        Returns:
        - JsonResponse: JSON response indicating logout status.
        """
        logout(request)
        return JsonResponse({"detail": "Successfully logged out."}, status=200)

