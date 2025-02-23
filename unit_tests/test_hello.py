from unit_tests.hello import hello

def test_default():
    assert hello() == "hello, world"
    

def test_argument():
    assert hello("Devid") == "hello, Devid"


# we can check using loop also (bunch of list)
def test_list_Of_Name():
    for name in ["ritam","sayak","rimu","pradip"]:
        assert hello(name) == f"hello, {name}"