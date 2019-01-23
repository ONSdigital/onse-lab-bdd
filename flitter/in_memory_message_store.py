class InMemoryMessageStore:
    def __init__(self):
        self.messages = []

    def add(self, message):
        self.messages.append(message)

    def fetch_by(self, user):
        return self.messages
