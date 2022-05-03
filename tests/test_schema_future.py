# Python 2/3

from __future__ import absolute_import, division, print_function, unicode_literals  # isort:skip

from future import standard_library  # isort:skip
from future.builtins import *  # noqa isort:skip
from future.builtins.disabled import *  # noqa isort:skip

standard_library.install_aliases()  # isort:skip

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