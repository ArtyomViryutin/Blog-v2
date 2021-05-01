from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied
from django.http import Http404


class AuthorPermissionMixin:
    def has_permission(self):
        return self.get_object().author == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
