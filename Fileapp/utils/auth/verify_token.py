# -*- coding: utf-8 -*-
from Fileapp.utils.jwt.jwt_encoder_decoder import JWTManager
from Fileapp.utils.response_handler.response_handler import AuthorizationError


def verify_token(request):    # method to verify whether the user is authorized or not
    try:
        # decode the token received in headers
        decoded_header = JWTManager().decode(encoded_jwt=request.headers.get('AUTHORIZATION')[7:])

        if not decoded_header:
            raise AuthorizationError('You are not authorized to access data')

        # verify user in system
        request.context.user_id = decoded_header.get('user_id', None)
        return True

    except KeyError:
        raise AuthorizationError('You are not authorized to access data')


def login_required(req, resp, resource, params):
    verify_token(request=req)
    return login_required
