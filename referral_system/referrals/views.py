from rest_framework import viewsets
from .models import CustomUser
from .serializers import UserSerializer
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


def profile(request):
    return render(request, 'profile.html')


@cache_page(60 * 5)  # Cache for 5 minutes
def my_cached_view(request):
    context = {
        'message': 'This content is cached and will be updated after 5 minutes.',
    }
    return render(request, 'profile.html', context)


def register(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        invite_code = request.POST.get('invite_code')

        # Check if user already exists
        user_exists = CustomUser.objects.filter(phone_number=phone_number).exists()

        if not user_exists:
            # Create a new user if not exists
            new_user = CustomUser(phone_number=phone_number, invite_code=invite_code)
            new_user.save()

        return redirect('profile')  # Redirect to the user's profile page

    return render(request, 'register.html')  # Render the registration form


def api_documentation(request):
    return render(request, 'api_documentation.html')