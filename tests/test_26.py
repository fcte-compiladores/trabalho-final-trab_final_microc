from microC import *
from microC import testing
from microC.ast import *


class TestExamplesReturn(testing.ExampleTester):
    module = "return"


class TestExamplesThis(testing.ExampleTester):
    module = "this"


class TestExamplesSuper(testing.ExampleTester):
    module = "super"
