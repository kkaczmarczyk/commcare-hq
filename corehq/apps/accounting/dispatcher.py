from django.utils.decorators import method_decorator
from corehq import toggles, privileges
from corehq.apps.reports.dispatcher import ReportDispatcher
from django_prbac.decorators import requires_privilege_raise404
from toggle.decorators import require_toggle


class AccountingAdminInterfaceDispatcher(ReportDispatcher):
    prefix = 'accounting_admin_interface'
    map_name = "ACCOUNTING_ADMIN_INTERFACES"

    @method_decorator(requires_privilege_raise404(privileges.ACCOUNTING_ADMIN))
    def dispatch(self, request, *args, **kwargs):
        return super(AccountingAdminInterfaceDispatcher, self).dispatch(request, *args, **kwargs)
