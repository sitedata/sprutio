from core import FM
from core.FMOperation import FMOperation


class FindText(FM.BaseAction):
    def __init__(self, request, params, session, **kwargs):
        super(FindText, self).__init__(request=request, **kwargs)

        self.params = params
        self.session = session

    def run(self):
        request = self.get_rpc_request()
        operation = FMOperation.create(FM.Action.FIND_TEXT, FMOperation.STATUS_WAIT)

        result = request.request('sftp/find_text', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), status_id=operation.id,
                                 params=self.params, session=self.session)
        answer = self.process_result(result)
        answer["data"] = operation.as_dict()
        return answer
