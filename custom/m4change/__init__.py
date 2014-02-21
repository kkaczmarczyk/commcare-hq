from custom.m4change.reports import anc_hmis_report
from custom.m4change.reports import project_indicators_report


CUSTOM_REPORTS = (
    ('Custom Reports', (
        anc_hmis_report.AncHmisReport,
        project_indicators_report.ProjectIndicatorsReport
    )),
)
