# Django Library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _

# Localfolder Library
from ..models import PyProductBrand
from .web_father import (
    FatherCreateView,
    FatherDeleteView,
    FatherDetailView,
    FatherListView,
    FatherUpdateView,
)

OBJECT_LIST_FIELDS = [
    {"string": _("Name"), "field": "name"},
]

OBJECT_FORM_FIELDS = ["name"]


class ProductBrandListView(LoginRequiredMixin, FatherListView):
    model = PyProductBrand
    template_name = "core/list.html"
    extra_context = {"fields": OBJECT_LIST_FIELDS}


class ProductBrandDetailView(LoginRequiredMixin, FatherDetailView):
    model = PyProductBrand
    template_name = "core/detail.html"
    extra_context = {"fields": OBJECT_LIST_FIELDS}


class ProductBrandCreateView(LoginRequiredMixin, FatherCreateView):
    model = PyProductBrand
    fields = OBJECT_FORM_FIELDS
    template_name = "core/form.html"


class ProductBrandUpdateView(LoginRequiredMixin, FatherUpdateView):
    model = PyProductBrand
    fields = OBJECT_FORM_FIELDS
    template_name = "core/form.html"


class ProductBrandDeleteView(LoginRequiredMixin, FatherDeleteView):
    model = PyProductBrand
