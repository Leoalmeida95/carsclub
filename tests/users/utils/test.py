from apps.utils import enums
from enum import EnumMeta


def test_enums_must_have_status_code():
    assert hasattr(enums, 'EStatus_Code')


def test_enums_status_code_must_be_callable():
    status_code = getattr(enums, 'EStatus_Code')
    assert hasattr(status_code, '__call__')


def test_enums_status_code_must_be_enum():
    status_code = getattr(enums, 'EStatus_Code')

    assert type(status_code) is EnumMeta


def test_enums_status_code_ok_is_200():
    assert enums.EStatus_Code.OK.value == 200


def test_enums_status_code_data_invalid_is_422():
    assert enums.EStatus_Code.DATA_INVALID.value == 422


def test_enums_status_code_exception_is_500():
    assert enums.EStatus_Code.EXCEPTION.value == 500


def test_enums_status_code_not_found_is_404():
    assert enums.EStatus_Code.NOT_FOUND.value == 404


def test_enums_status_code_bad_request_is_400():
    assert enums.EStatus_Code.BAD_REQUEST.value == 400
