from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class UserStorage(models.Model):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("User Storage")
        verbose_name_plural = _("User Storage Records")