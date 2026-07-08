'''
# Example test
def test_example(mocker):
    greeter = Greeter()
    mocker.patch.object(greeter, "some_method", return_value="some value")

    result = greeter.some_method()

    assert result == "some value"

'''
from greeter import Greeter


# Test that greet() returns "Good morning, Alice!"
# when the hour is 9 and the user_id is 1 (Alice).
def test_greet_morning(mocker):
    greeter = Greeter()
    mocker.patch.object(greeter, "get_current_hour", return_value=9)
    mocker.patch.object(greeter, "get_username", return_value="Alice")

    result = greeter.greet(1)

    assert result == "Good morning, Alice!"

# Test that greet() returns "Good afternoon, Bob!"
# when the hour is 14 and the user_id is 2 (Bob).
def test_greet_afternoon(mocker):
    greeter = Greeter()
    mocker.patch.object(greeter, "get_current_hour", return_value=14)
    mocker.patch.object(greeter, "get_username", return_value="Bob")

    result = greeter.greet(2)

    assert result == "Good afternoon, Bob!"


# Test that greet() returns "Good evening, Guest!"
# when the hour is 21 and the user_id is 99 (unknown user).
def test_greet_evening_unknown_user(mocker):
    greeter = Greeter()
    mocker.patch.object(greeter, "get_current_hour", return_value=21)
    mocker.patch.object(greeter, "get_username", return_value="Guest")

    result = greeter.greet(99)

    assert result == "Good evening, Guest!"
    


# Stretch goal
# Add a test that checks greet() still works correctly at
# exactly hour=5 (the boundary between "evening" and "morning").
# What does the greeting say? Is that the right behaviour?
def test_morning_boundary_hour_five(mocker):
    greeter = Greeter()

    mocker.patch.object(greeter, "get_current_hour", return_value=5)
    mocker.patch.object(greeter, "get_username", return_value="Alice")

    result = greeter.greet(1)

    assert result == "Good morning, Alice!"