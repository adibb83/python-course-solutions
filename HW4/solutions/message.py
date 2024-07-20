import uuid


class Message:
    def __init__(self, from_actor: str, to_actor: str, desc: str):
        self.id = str(uuid.uuid4())
        self.from_actor = from_actor
        self.to_actor = to_actor
        self.message_desc = desc
