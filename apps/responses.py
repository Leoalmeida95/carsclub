# -*- coding: utf-8 -*-

from flask import jsonify

from .messages import MSG_INVALID_DATA, MSG_DOES_NOT_EXIST, MSG_EXCEPTION
from .messages import MSG_ALREADY_EXISTS
from .utils.enums import EStatus_Code


def resp_data_invalid(
    resource: str, errors: dict, msg: str = MSG_INVALID_DATA
):
    '''
    Responses 422 Unprocessable Entity
    '''

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')

    resp = jsonify({
        'resource': resource,
        'message': msg,
        'errors': errors,
    })

    resp.status_code = EStatus_Code.DATA_INVALID.value

    return resp


def resp_exception(
    resource: str, description: str = '', msg: str = MSG_EXCEPTION
):
    '''
    Responses 500
    '''

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')

    resp = jsonify({
        'resource': resource,
        'message': msg,
        'description': description
    })

    resp.status_code = EStatus_Code.EXCEPTION.value

    return resp


def resp_does_not_exist(
    resource: str, description: str
):
    '''
    Responses 404 Not Found
    '''

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')

    resp = jsonify({
        'resource': resource,
        'message': MSG_DOES_NOT_EXIST.format(description),
    })

    resp.status_code = EStatus_Code.NOT_FOUND.value

    return resp


def resp_already_exists(
    resource: str, description: str
):
    '''
    Responses 400
    '''

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')

    resp = jsonify({
        'resource': resource,
        'message': MSG_ALREADY_EXISTS.format(description),
    })

    resp.status_code = EStatus_Code.BAD_REQUEST.value

    return resp


def resp_ok(
    resource: str, message: str, data=None, **extras
):
    '''
    Responses 200
    '''

    response = {'status': EStatus_Code.OK.value,
                'message': message,
                'resource': resource
                }

    if data:
        response['data'] = data

    response.update(extras)

    resp = jsonify(response)

    resp.status_code = EStatus_Code.OK.value

    return resp
