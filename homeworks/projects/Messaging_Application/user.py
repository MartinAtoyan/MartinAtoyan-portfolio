from typing import List

from orca.chat import Conversation
import message
from homeworks.projects.Messaging_Application.message import Message


class User:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.conversations: List['Conversation'] = []

    def create_conversation(self, user: 'User') -> 'Conversation':
        conversation = Conversation([self, user])
        self.conversations.append(conversation)
        user.conversations.append(conversation)
        print(f"Conversation created between {self.name} and {user.name}.")
        return conversation

    def send_message(self, message: 'Message', conversation: 'Conversation') -> None:
        conversation.add_message(message)
        print(f"{self.name} sent a message to the conversation.")

    def receive_message(self, message: 'Message') -> None:
        print(f"{self.name} received a message from {message.sender.name}: {message.display_content()}")

    def manage_settings(self) -> None:
        print(f"{self.name} is managing settings.")

    def get_conversations(self) -> List['Conversation']:
        return self.conversations


class Conversation:
    def __init__(self, participants: List['User']):
        self.participants = participants
        self.message_history: List['Message'] = []

    def add_message(self, message: 'Message') -> None:
        self.message_history.append(message)
        for participant in self.participants:
            if participant != message.sender:
                participant.receive_message(message)
        print(f"Message added to conversation by {message.sender.name}.")

    def add_user(self, user: 'User') -> None:
        self.participants.append(user)
        print(f"{user.name} added to the conversation.")

    def get_messages(self) -> List['Message']:
        return self.message_history

