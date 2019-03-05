from flitter.in_memory_message_store import InMemoryMessageStore
from flitter.message import Message


def test_fetch_by_author_returns_a_list():
    store = InMemoryMessageStore()

    assert store.fetch_by_author('alice') == []


def test_fetch_by_author_returns_messages_by_the_author():
    message1 = Message(author='alice', text='hi1')
    message2 = Message(author='alice', text='hi2')
    store = InMemoryMessageStore()

    store.save(message1)
    store.save(message2)

    messages = store.fetch_by_author('alice')

    assert message1 in messages, f'{message1} was not in {messages}'
    assert message2 in messages, f'{message2} was not in {messages}'
