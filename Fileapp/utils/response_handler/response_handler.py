from json import dumps


class ResponseEngine:
    def __init__(self, response, body):
        if not body:
            body = {}
        response_dict = {'msg': body}
        self.response = response
        self.response.status = 422
        self.response_dict = response_dict

    def success_response(self):
        self.response.status = 200
        self.response.text = dumps(self.response_dict)

    def error_response_with_message(self, msg_error):
        self.response_dict['msg']['error'] = msg_error
        self.response.text = dumps(self.response_dict)
