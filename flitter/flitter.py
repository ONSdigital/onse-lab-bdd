from flitter.message import Message


class Flitter:
    def __init__(self, message_store):
        self.message_store = message_store

    def post(self, author, message):
        self.message_store.save(Message(author=author, text=message))

    def get_feed_for(self, user):
        feed = []

        for message in self.message_store.fetch_by_author(user):
            feed.append(dict(author=message.author, message=message.text))

        return feed

    def follow(self, follower, followee):
        """
        Make one user follow another
        :param follower: The user who is following
        :type follower: string
        :param followee:  The user being followed
        :type followee: string
        :return: nothing
        :rtype: void
        """
        pass
