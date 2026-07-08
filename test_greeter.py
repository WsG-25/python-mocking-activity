from greeter import Greeter


# Test that greet() returns "Good morning, Alice!"
# when the hour is 9 and the user_id is 1 (Alice).
def test_greet_morning(mocker):
    pass


# Test that greet() returns "Good afternoon, Bob!"
# when the hour is 14 and the user_id is 2 (Bob).
def test_greet_afternoon(mocker):
    pass


# Test that greet() returns "Good evening, Guest!"
# when the hour is 21 and the user_id is 99 (unknown user).
def test_greet_evening_unknown_user(mocker):
    pass


# Stretch goal
# Add a test that checks greet() still works correctly at
# exactly hour=5 (the boundary between "evening" and "morning").
# What does the greeting say? Is that the right behaviour?
