import pytest

from microC import *
from microC import testing
from microC.ast import *


@pytest.mark.full_suite
class TestExamplesClass(testing.ExampleTester):
    module = "class"
