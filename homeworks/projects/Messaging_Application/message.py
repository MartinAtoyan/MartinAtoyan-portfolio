import abc
from datetime import datetime
from homeworks.projects.Messaging_Application.user import User, Conversation


class Message(abc.ABC):
    def __init__(self, sender: 'User', conversation: 'Conversation'):
        self.sender = sender
        self.conversation = conversation
        self.timestamp = datetime.now()

    @abc.abstractmethod
    def display_content(self) -> None:
        ...

    @abc.abstractmethod
    def get_message_type(self) -> str:
        ...


class TextMessage(Message):
    def __init__(self, sender: 'User', conversation: 'Conversation', content: str):
        super().__init__(sender, conversation)
        self.content = content

    def display_content(self) -> None:
        print(f"Text Message from {self.sender.name}: {self.content}. {self.timestamp})")

    def get_message_type(self) -> str:
        return "Text"


class MultimediaMessage(Message):
    def __init__(self, sender: 'User', conversation: 'Conversation', file_path: str, media_type: str):
        super().__init__(sender, conversation)
        self.file_path = file_path
        self.media_type = media_type

    def display_content(self) -> None:
        print(f"Multimedia message from {self.sender.name}: {self.media_type}, {self.file_path}. {self.timestamp})")

    def get_message_type(self) -> str:
        return self.media_type
