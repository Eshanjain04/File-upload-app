# -*- coding: utf-8 -*-
from Fileapp.utils.jwt.jwt_encoder_decoder import JWTManager


def verify_token(request):
    try:
        decoded_header = JWTManager().decode(encoded_jwt=request.headers['AUTHORIZATION'][7:])

        if not decoded_header:
            raise ValueError('Unauthorised access')

        # verify user in system
        request.context.user_id = decoded_header.get('user_id', None)
        return True

    except KeyError:
        raise ValueError('Unauthorised access')


def login_required(req, resp, resource, params):
    verify_token(request=req)
    return login_required
