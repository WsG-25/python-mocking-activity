from datetime import datetime


class Greeter:

    def get_current_hour(self):
        """Returns the current hour as an integer (0–23)."""
        return datetime.now().hour

    def get_username(self, user_id):
        """Returns the display name for a given user ID."""
        users = {
            1: "Alice",
            2: "Bob",
            3: "Charlie",
        }
        return users.get(user_id, "Guest")

    def greet(self, user_id):
        """Returns a time-appropriate greeting for the given user."""
        hour = self.get_current_hour()
        name = self.get_username(user_id)

        if 5 <= hour < 12:
            period = "morning"
        elif 12 <= hour < 18:
            period = "afternoon"
        else:
            period = "evening"

        return f"Good {period}, {name}!"
