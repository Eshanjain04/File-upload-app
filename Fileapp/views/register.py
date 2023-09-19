from Fileapp.models.user import User
from Fileapp.utils.password_hashing import Encrypt
from Fileapp.utils.response_handler.response_handler import ResponseEngine


class Register:

    def on_post(self, request, response):
        user_input = request.media
        body = {'status': 'failed', 'msg': ''}
        if not (user_input.get('user_name')):
            body['msg'] = 'Please Enter Username'
            return ResponseEngine(response=response, body=body).error_response()
        elif not user_input.get('email'):
            body['msg'] = 'Please Enter Email'
            return ResponseEngine(response=response, body=body).error_response()
        elif not user_input.get('password'):
            body['msg'] = 'Please Enter Password'
            return ResponseEngine(response=response, body=body).error_response()
        user_obj_with_user_name = User.objects.filter(user_name=user_input['user_name']).first()
        user_obj_with_email = User.objects.filter(user_name=user_input['email']).first()
        if user_obj_with_user_name or user_obj_with_email:
            body['msg'] = 'User Already Exists with given username/email'
            return ResponseEngine(response=response, body=body).error_response()
        else:
            hash_pass = Encrypt().encrypt(user_input.get('password'))
            new_user_obj = User(user_name=user_input['user_name'],
                                email=user_input['email'],
                                password=hash_pass)
            new_user_obj.save()
            return ResponseEngine(response=response, body=new_user_obj.to_dict).success_response()
