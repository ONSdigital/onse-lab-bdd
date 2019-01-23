import pytest

from flitter.in_memory_message_store import InMemoryMessageStore
from flitter.message import Message


@pytest.fixture
def message_store():
    return InMemoryMessageStore()


def test_fetch_by_returns_a_list(message_store):
    assert type(message_store.fetch_by('bob')) is list


def test_fetch_by_returns_the_messages_by_a_given_user(message_store):
    message1 = Message(author='bob', text='hi1')
    message2 = Message(author='bob', text='hi2')
    message_store.add(message1)
    message_store.add(message2)

    messages = message_store.fetch_by('bob')

    assert message1 in messages
    assert message2 in messages