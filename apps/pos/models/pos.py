# Django Library
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Thirdparty Library
from apps.core.models import PyFather


class PyPos(PyFather):
    name = models.CharField("Nombre", max_length=80)

    def get_absolute_url(self):
        return reverse("pos:pos-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return format(self.name)
