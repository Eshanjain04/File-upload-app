from Fileapp.models.user import User
from Fileapp.utils.password_hashing import Encrypt
from Fileapp.utils.response_handler.response_handler import ResponseEngine


class Register:

    def on_post(self, request, response):
        user_input = request.media
        if not (user_input.get('user_name')):
            return ResponseEngine(response=response, body='Please Enter Username').error_response()
        elif not user_input.get('email'):
            return ResponseEngine(response=response, body='Please Enter Email').error_response()
        elif not user_input.get('password'):
            return ResponseEngine(response=response, body='Please Enter Password').error_response()
        user_obj = User.objects.filter(user_name=user_input['user_name']).first()
        if user_obj:
            return ResponseEngine(response=response, body='User Already Exists').error_response()
        else:
            hash_pass = Encrypt().encrypt(user_input.get('password'))
            new_user_obj = User(user_name=user_input['user_name'],
                                email=user_input['email'],
                                password=hash_pass)
            new_user_obj.save()
            return ResponseEngine(response=response, body=new_user_obj.to_dict).success_response()
