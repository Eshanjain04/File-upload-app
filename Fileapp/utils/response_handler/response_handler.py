from json import dumps
import falcon


class ResponseEngine:  # class to handle success and error response by api and make it generic
    def __init__(self, response, body):
        if not body:
            body = {}
        response_dict = {'msg': body}
        self.response = response
        self.response_dict = response_dict

    def success_response(self):  # success response handler with 200 status code
        self.response.status = 200
        self.response.text = dumps(self.response_dict)

    def error_response(self):  # error response handler with 422 status code
        self.response.status = 422
        self.response.text = dumps(self.response_dict)


class AuthorizationError(
    falcon.HTTPError):  # class to handle raising unauthorized access error and give proper response
    def __init__(self, message):
        super().__init__(
            status=falcon.HTTP_422,
            title='Authorization Error',
            description=message
        )
