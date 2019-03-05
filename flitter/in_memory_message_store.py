class InMemoryMessageStore:
    def __init__(self):
        self.messages = []

    def save(self, message):
        self.messages.append(message)

    def fetch_by_author(self, author):
        return self.messages
