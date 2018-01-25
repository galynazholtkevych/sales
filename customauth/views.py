from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from rest_framework.response import SimpleTemplateResponse, Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from .forms import AuthenticationForm, RegisterForm

from .serializers import LoginSerializer


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'customauth/templates/register.html'
    success_url = reverse_lazy('customers:create_customer')

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password2')
        authenticated = authenticate(username=username, password=raw_password)
        if authenticated:
            login(self.request, authenticated)
            return super(RegisterView, self).form_valid(form)


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'customauth/templates/login.html'
    success_url = reverse_lazy('customers:create_customer')

    def post(self, request, *args, **kwargs):
        is_valid = super(LoginView, self).post(request, *args, **kwargs)
        form = self.get_form()
        print("form data@!!! ", form.data)
        print("!cleaned data>>> ", form.cleaned_data)
        #form.clean()
        # return user to the context
        return is_valid


class APILoginView(GenericAPIView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer

    def post(self, request):
        self.serializer_class(data=request.data).is_valid(raise_exception=True)
        username = request.data.get('username')
        password = request.data.get('password')

        authenticated = authenticate(username=username,
                                     password=password)
        if authenticated:
            return SimpleTemplateResponse("index.html")
        return Response(status=HTTP_401_UNAUTHORIZED)
