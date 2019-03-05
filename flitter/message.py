class Message:
    def __init__(self, author, text):
        self.author = author
        self.text = text

    def __repr__(self):
        return f'Message(author={self.author}, text={self.text})'
