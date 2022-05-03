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
    }


def test_optional_map_type(json_schema):
    payload = {"optional_map": {"my_bool": True}}
    with pytest.raises(SchemaError):
        Schema(json_schema, ignore_extra_keys=True).validate(payload)