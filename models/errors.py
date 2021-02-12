
class MyValueError(Exception):
    def __init__(self, msg):
        self.text = msg