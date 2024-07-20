from HW4.solutions.message import Message


class CommunicationService:

    def send_message(self, message: Message) -> None:
        print(f"Message sent: {message.id , message.from_actor, message.to_actor, message.message_desc}")

    def receive_message(self) -> None:
        print("Message received")

    def __repr__(self):
        return f"({self.__dict__})"
