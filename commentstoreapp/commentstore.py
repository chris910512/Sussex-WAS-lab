from queue import Queue
from .comment import Comment


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class CommentStore:
    commentlist = Queue()

    def insertcomment(self, name, date, comment):
        comment = Comment(name, date, comment)
        self.commentlist.put(comment)
