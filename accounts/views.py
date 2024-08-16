from django.contrib.auth import logout, authenticate, login
from django.http import JsonResponse
from django.views import View
from django.middleware.csrf import get_token

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    
    def post(self, request):
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
    def post(self, request):
        logout(request)
        return JsonResponse({"detail": "Successfully logged out."}, status=200)

