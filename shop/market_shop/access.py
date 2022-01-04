from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages
from django.core.exceptions import PermissionDenied, ImproperlyConfigured
from django.shortcuts import redirect
from django.contrib.auth.views import redirect_to_login
from market_user.models import CustomUser


class ActiveOnlyMixin(AccessMixin):
    

    def get_not_activated_message(self):
        return self.not_activated_message

    def handle_not_activated(self):
        """ Deal with users that are logged in but not activated yet. """
        message = self.get_not_activated_message()
        if self.raise_exception:
            raise PermissionDenied(message)
        messages.error(self.request, message)
        return redirect(self.get_not_activated_redirect())

    def get_not_activated_redirect(self):
        if not self.not_activated_redirect:
            raise ImproperlyConfigured(
                '{0} is missing the not_activated_redirect attribute. Define {0}.not_activated_redirect, or override '
                '{0}.get_not_activated_redirect().'.format(self.__class__.__name__))
        return self.not_activated_redirect

    def handle_no_permission(self):
        """ Overwrite to allow a message to be sent. """
        message = self.get_permission_denied_message()
        if self.raise_exception:
            raise PermissionDenied(message)
        messages.error(self.request, message)
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())

    def dispatch(self, request, *args, **kwargs):
        user_type = CustomUser.objects.get(email=request.user).user_type_owner_shop
        if not user_type:
            return self.handle_no_permission()
        # if not request.user.is_authenticated():
        #     return self.handle_no_permission()
        # if not request.user.is_active:
        #     return self.handle_not_activated()
        return super(ActiveOnlyMixin, self).dispatch(request, *args, **kwargs)