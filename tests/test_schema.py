import pytest

from schema import Optional
from schema import Or
from schema import Schema
from schema import SchemaError


@pytest.fixture()
def json_schema():
    return {
        Optional("optional_map"): {
            str: Or(str, int)
        },
        "str_or_int": Or(str, int),
    }


def test_optional_map_type(json_schema):
    payload = {"optional_map": {"my_bool": True}, "str_or_int": 123}
    with pytest.raises(SchemaError):
        Schema(json_schema, ignore_extra_keys=True).validate(payload)


def test_or_type(json_schema):
    payload = {"str_or_int": True}
    with pytest.raises(SchemaError):
        Schema(json_schema, ignore_extra_keys=True).validate(payload)
