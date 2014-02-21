from django.utils.translation import ugettext as _
from sqlagg import SumColumn
from corehq.apps.reports.sqlreport import SqlData, DatabaseColumn


class AncHmisCaseSqlData(SqlData):

    table_name = "fluff_AncHmisCaseFluff"

    def __init__(self, domain, datespan):
        self.domain = domain
        self.datespan = datespan

    @property
    def filter_values(self):
        return dict(
            domain=self.domain,
            startdate=self.datespan.startdate_utc.date(),
            enddate=self.datespan.enddate_utc.date()
        )

    @property
    def filters(self):
        return [
            "domain = :domain",
            "date between :startdate and :enddate"
        ]

    @property
    def columns(self):
        return [
            DatabaseColumn(_("Antenatal Attendance - Total"), SumColumn("attendance_total")),
            DatabaseColumn(_("Antenatal first Visit before 20wks"), SumColumn("attendance_before_20_weeks_total")),
            DatabaseColumn(_("Antenatal first Visit after 20wks"), SumColumn("attendance_after_20_weeks_total")),
            DatabaseColumn(_("Pregnant Women that attend antenatal clinic for 4th visit during the month"),
                           SumColumn("attendance_gte_4_visits_total")),
            DatabaseColumn(_("ANC syphilis test done"), SumColumn("anc_syphilis_test_done_total")),
            DatabaseColumn(_("ANC syphilis test positive"), SumColumn("anc_syphilis_test_positive_total")),
            DatabaseColumn(_("ANC syphilis case treated"), SumColumn("anc_syphilis_case_treated_total")),
            DatabaseColumn(_("Pregnant women who receive malaria IPT1"), SumColumn("pregnant_mothers_receiving_ipt1_total")),
            DatabaseColumn(_("Pregnant women who receive malaria IPT2"), SumColumn("pregnant_mothers_receiving_ipt2_total")),
            DatabaseColumn(_("Pregnant women who receive malaria LLIN"), SumColumn("pregnant_mothers_receiving_llin_total")),
            DatabaseColumn(_("Pregnant women who receive malaria Haematinics"), SumColumn("pregnant_mothers_receiving_ifa_total")),
            DatabaseColumn(_("Postanatal Attendance - Total"), SumColumn("postnatal_attendance_total")),
            DatabaseColumn(_("Postnatal clinic visit within 1 day of delivery"), SumColumn("postnatal_clinic_visit_lte_1_day_total")),
            DatabaseColumn(_("Postnatal clinic visit within 3 days of delivery"), SumColumn("postnatal_clinic_visit_lte_3_days_total")),
            DatabaseColumn(_("Postnatal clinic visit >= 7 days of delivery"), SumColumn("postnatal_clinic_visit_gte_7_days_total"))
        ]

    @property
    def group_by(self):
        return ['domain']


class ProjectIndicatorsCaseSqlData(SqlData):

    table_name = "fluff_ProjectIndicatorsCaseFluff"

    def __init__(self, domain, datespan):
        self.domain = domain
        self.datespan = datespan

    @property
    def filter_values(self):
        return dict(
            domain=self.domain,
            startdate=self.datespan.startdate_utc.date(),
            enddate=self.datespan.enddate_utc.date()
        )

    @property
    def filters(self):
        return [
            "domain = :domain",
            "date between :startdate and :enddate"
        ]

    @property
    def columns(self):
        return [
            DatabaseColumn(_("Number of pregnant women who registered for ANC (in CCT payment sites only) "),
                           SumColumn("pregnant_mothers_registered_ANC")),
            DatabaseColumn(_("Number of women who received payment for ANC registration"),
                           SumColumn("women_receiving_payment_ANC")),
            DatabaseColumn(_("Number of women who received payment for ANC registration within two weeks"),
                           SumColumn("women_receiving_payment_ANC_2_weeks")),
            DatabaseColumn(_("Number of women who had 4 ANC visits (in CCT payment sites only)"),
                           SumColumn("women_having_4_ANC_visits")),
            DatabaseColumn(_("Number of women who received payment for 4 ANC visits"),
                           SumColumn("women_receiving_payment_4_ANC_visits")),
            DatabaseColumn(_("Number of women who received payment for 4 ANC visits within two weeks"),
                           SumColumn("women_receiving_payment_4_ANC_visits_2_weeks")),
            DatabaseColumn(_("Number of women who delivered at the facility (in CCT payment sites only)"),
                           SumColumn("women_delivering_at_the_facility")),
            DatabaseColumn(_("Number of women who received payment for delivery at the facility"),
                           SumColumn("women_delivering_at_the_facility_receiving_payment")),
            DatabaseColumn(_("Number of women who received payment for delivery at the facility within two weeks"),
                           SumColumn("women_delivering_at_the_facility_receiving_payment_2_weeks")),
            DatabaseColumn(_("Number of women who attended PNC within 6 weeks of delivery"),
                           SumColumn("women_delivering_within_6_weeks_attending_PNC")),
            DatabaseColumn(_("Number of women who received payment for attending PNC within 6 weeks of delivery"),
                           SumColumn("women_delivering_within_6_weeks_attending_PNC_receiving_payment")),
            DatabaseColumn(_("Number of women who received payment for attending PNC within 6 weeks of delivery within two weeks"),
                           SumColumn("women_delivering_within_6_weeks_attending_PNC_receiving_payment_within_2_weeks"))
        ]

    @property
    def group_by(self):
        return ['domain']



