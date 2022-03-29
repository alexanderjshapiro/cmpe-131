from tracker import *


@func_counter
def foo(bar):
    print(bar)


def test_tracker():
    foo("baz")
    foo("qux")
    assert foo.counter == 2
