import abc
from homeworks.projects.Messaging_Application.Conversation_user import Conversation
from homeworks.projects.Messaging_Application.message import Message


class MessagingManager(abc.ABC):
    @abc.abstractmethod
    def send_message(self, message: 'Message') -> None:
        ...

    @abc.abstractmethod
    def receive_message(self, message: 'Message') -> None:
        ...

    @abc.abstractmethod
    def view_conversation_history(self, conversation: 'Conversation') -> list['Message']:
        ...
