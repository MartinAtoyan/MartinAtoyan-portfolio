from homeworks.projects.Messaging_Application.message import Message
from homeworks.projects.Messaging_Application.user import User


class Conversation:
    def __init__(self, participants: list['User']):
        self.participants = participants
        self.message_history: list['Message'] = []

    def add_message(self, message: 'Message') -> None:
        self.message_history.append(message)
        for participant in self.participants:
            if participant != message.sender:
                participant.receive_message(message)
        print(f"Message added to conversation by {message.sender.name}.")

    def add_user(self, user: 'User') -> None:
        self.participants.append(user)
        print(f"{user.name} added to the conversation.")

    def get_messages(self) -> list['Message']:
        return self.message_history
