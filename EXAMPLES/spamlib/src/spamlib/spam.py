"""
Subjects for testing
"""
import re
from hamlib import ham  

class Spam():
    def __init__(self, number):
        self._value = ham(number)

    @property
    def value(self):
        return self._value


class SpamSearch():  # System under test
    def __init__(self, search_string, target_string):
        self.search_string = search_string
        self.target_string = target_string

    def findit(self):  # Specific method to test (uses re.search)
        return re.search(self.target_string, self.search_string)


if __name__ == "__main__":
    s = Spam(42)
    print(f"{s.value = }")
    
    srch = SpamSearch("lightning bug", "bug")
    print(f"{srch.findit() = }")
    
