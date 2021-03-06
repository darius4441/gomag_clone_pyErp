# Django Library
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Localfolder Library
from .father import PyFather


class PyFaq(PyFather):
    name = models.CharField(_("Name"), max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Faq")
        verbose_name_plural = _("Faqs")
