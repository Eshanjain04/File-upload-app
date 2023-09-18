class Register:
    def __init__(self):
        pass

    def on_get(self, request, response):
        response.media = {'msg': 'Success'}
        return response
