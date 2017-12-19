from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CustomauthConfig(AppConfig):
    name = 'customauth'
    verbose_name = _('Custom Authentication')
