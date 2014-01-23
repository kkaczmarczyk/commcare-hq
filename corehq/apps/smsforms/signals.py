from touchforms.formplayer.signals import sms_form_complete
from corehq.apps.receiverwrapper.util import submit_form_locally
from couchforms.models import XFormInstance


def handle_sms_form_complete(sender, session_id, form, **kwargs):
    from corehq.apps.smsforms.models import XFormsSession
    session = XFormsSession.latest_by_session_id(session_id)
    if session:
        # i don't know if app_id is the id of the overall app or the id of the specific build of the app
        # the thing i want to pass in is the id of the overall app
        resp = submit_form_locally(
            instance=form,
            domain=session.domain,
            app_id=session.app_id,
        )
        xform_id = resp['X-CommCareHQ-FormID']
        session.end(completed=True)
        session.submission_id = xform_id
        session.save()
        
        xform = XFormInstance.get(xform_id)
        xform.survey_incentive = session.survey_incentive
        xform.save()

sms_form_complete.connect(handle_sms_form_complete)
