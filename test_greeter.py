
from greeter import Greeter

def test_greet_morning(mocker):
    greeter = Greeter()
    mocker.patch.object(greeter, "get_current_hour", return_value=9)
    mocker.patch.object(greeter, "get_username", return_value="Alice")

    result = greeter.greet(1)

    assert result == "Good morning, Alice!"

def test_greet_afternoon(mocker):
    greeter = Greeter()
    mocker.patch.object(greeter, "get_current_hour", return_value=14)
    mocker.patch.object(greeter, "get_username", return_value="Bob")

    result = greeter.greet(2)

    assert result == "Good afternoon, Bob!"

def test_greet_evening_unknown_user(mocker):
    greeter = Greeter()
    mocker.patch.object(greeter, "get_current_hour", return_value=21)
    mocker.patch.object(greeter, "get_username", return_value="Guest")

    result = greeter.greet(99)

    assert result == "Good evening, Guest!"
    
def test_morning_boundary_hour_five(mocker):
    greeter = Greeter()

    mocker.patch.object(greeter, "get_current_hour", return_value=5)
    mocker.patch.object(greeter, "get_username", return_value="Alice")

    result = greeter.greet(1)

    assert result == "Good morning, Alice!"