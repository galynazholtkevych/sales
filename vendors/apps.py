from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class VendorsConfig(AppConfig):
    name = 'vendors'
    verbose_name = _('Vendors')
