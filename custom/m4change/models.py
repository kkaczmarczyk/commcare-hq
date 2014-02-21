from casexml.apps.case.models import CommCareCase
import fluff
from custom.m4change import user_calcs


class AncHmisCaseFluff(fluff.IndicatorDocument):
    document_class = CommCareCase
    domains = ('m4change',)
    group_by = ('domain',)
    save_direct_to_sql = True

    attendance = user_calcs.AncAntenatalAttendanceCalculator()
    attendance_before_20_weeks = user_calcs.AncAntenatalVisitBefore20WeeksCalculator()
    attendance_after_20_weeks = user_calcs.AncAntenatalVisitAfter20WeeksCalculator()
    attendance_gte_4_visits = user_calcs.AncAttendanceGreaterEqual4VisitsCalculator()
    anc_syphilis_test_done = user_calcs.AncSyphilisTestDoneCalculator()
    anc_syphilis_test_positive = user_calcs.AncSyphilisPositiveCalculator()
    anc_syphilis_case_treated = user_calcs.AncSyphilisCaseTreatedCalculator()
    pregnant_mothers_receiving_ipt1 = user_calcs.PregnantMothersReceivingIpt1Calculator()
    pregnant_mothers_receiving_ipt2 = user_calcs.PregnantMothersReceivingIpt2Calculator()
    pregnant_mothers_receiving_llin = user_calcs.PregnantMothersReceivingLlinCalculator()
    pregnant_mothers_receiving_ifa = user_calcs.PregnantMothersReceivingIfaCalculator()
    postnatal_attendance = user_calcs.PostnatalAttendanceCalculator()
    postnatal_clinic_visit_lte_1_day = user_calcs.PostnatalClinicVisitWithin1DayOfDeliveryCalculator()
    postnatal_clinic_visit_lte_3_days = user_calcs.PostnatalClinicVisitWithin3DaysOfDeliveryCalculator()
    postnatal_clinic_visit_gte_7_days = user_calcs.PostnatalClinicVisitGreaterEqual7DaysOfDeliveryCalculator()


AncHmisCaseFluffPillow = AncHmisCaseFluff.pillow()


class ProjectIndicatorsReportSqlData(fluff.IndicatorDocument):
    document_class = CommCareCase
    domains = ('m4change',)
    group_by = ('domain',)
    save_direct_to_sql = True

    pregnant_mothers_registered_ANC = user_calcs.AncAntenatalAttendanceCalculator()
    women_receiving_payment_ANC = user_calcs.AncAntenatalVisitBefore20WeeksCalculator()
    women_receiving_payment_ANC_2_weeks = user_calcs.AncAntenatalVisitAfter20WeeksCalculator()
    women_having_4_ANC_visits = user_calcs.AncAttendanceGreaterEqual4VisitsCalculator()
    women_receiving_payment_4_ANC_visits = user_calcs.AncSyphilisTestDoneCalculator()
    women_receiving_payment_4_ANC_visits_2_weeks = user_calcs.AncSyphilisPositiveCalculator()
    women_delivering_at_the_facility = user_calcs.AncSyphilisCaseTreatedCalculator()
    women_delivering_at_the_facility_receiving_payment = user_calcs.PregnantMothersReceivingIpt1Calculator()
    women_delivering_at_the_facility_receiving_payment_2_weeks = user_calcs.PregnantMothersReceivingIpt2Calculator()
    women_delivering_within_6_weeks_attending_PNC = user_calcs.PregnantMothersReceivingLlinCalculator()
    women_delivering_within_6_weeks_attending_PNC_receiving_payment = user_calcs.PregnantMothersReceivingIfaCalculator()
    women_delivering_within_6_weeks_attending_PNC_receiving_payment_within_2_weeks = user_calcs.PostnatalAttendanceCalculator()
