from dimagi.utils.decorators.memoized import memoized
from django.utils.translation import ugettext as _
from corehq.apps.reports.datatables import DataTablesHeader, DataTablesColumn
from corehq.apps.reports.standard import MonthYearMixin, CustomProjectReport
from corehq.apps.reports.standard.cases.basic import CaseListReport
from custom.m4change.constants import DOMAIN
from custom.m4change.reports.sql_data import ProjectIndicatorsCaseSqlData


class ProjectIndicatorsReport(MonthYearMixin, CustomProjectReport, CaseListReport):
    ajax_pagination = False
    asynchronous = True
    exportable = True
    emailable = False
    name = "Project Indicators Report"
    slug = "facility_project_indicators_report"
    default_rows = 25

    @property
    def headers(self):
        headers = DataTablesHeader(DataTablesColumn(_("s/n")),
                                   DataTablesColumn(_("m4change Project Indicators")),
                                   DataTablesColumn(_("Total")))
        return headers

    @property
    def rows(self):
        self.form_sql_data = ProjectIndicatorsCaseSqlData(domain=DOMAIN, datespan=self.datespan)

        print(self.form_sql_data.data[DOMAIN])

        report_rows = [
            (23, _("Number of pregnant women who registered for ANC (in CCT payment sites only"), self.form_sql_data.data[DOMAIN].get("attendance_total", 0)),
            (24, _("Antenatal first Visit before 20wks"), self.form_sql_data.data[DOMAIN].get("attendance_before_20_weeks_total", 0)),
            (25, _("Antenatal first Visit after 20wks"), self.form_sql_data.data[DOMAIN].get("attendance_after_20_weeks_total", 0)),
            (26, _("Antenatal first visit - total"), antenatal_first_visit_total),
            (27, _("Pregnant Women that attend antenatal clinic for 4th visit during the month"),
                self.form_sql_data.data[DOMAIN].get("attendance_gte_4_visits_total", 0)),
            (28, _("ANC syphilis test done"), self.form_sql_data.data[DOMAIN].get('anc_syphilis_test_done_total', 0)),
            (29, _("ANC syphilis test positive"), self.form_sql_data.data[DOMAIN].get('anc_syphilis_test_positive_total', 0)),
            (30, _("ANC syphilis case treated"), self.form_sql_data.data[DOMAIN].get('anc_syphilis_case_treated_total', 0)),
            (31, _("Pregnant women who receive malaria IPT1"), self.form_sql_data.data[DOMAIN].get('pregnant_mothers_receiving_ipt1_total', 0)),
            (32, _("Pregnant women who receive malaria IPT2"),self.form_sql_data.data[DOMAIN].get('pregnant_mothers_receiving_ipt2_total', 0)),
            (33, _("Pregnant women who receive LLIN"), self.form_sql_data.data[DOMAIN].get('pregnant_mothers_receiving_llin_total', 0)),
            (34, _("Pregnant women who receive Haematinics"), self.form_sql_data.data[DOMAIN].get('pregnant_mothers_receiving_ifa_total', 0))
        ]

        for row in report_rows:
            value = row[2]
            if value is None:
                value = 0
            yield [row[0], row[1], value]

    @property
    @memoized
    def rendered_report_title(self):
        return self.name

