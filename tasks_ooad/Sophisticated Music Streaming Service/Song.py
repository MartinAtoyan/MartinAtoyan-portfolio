from abc import ABC, abstractmethod
from datetime import datetime

class function_of_player:
    def play(self):
        print("Play")

    def pause(self):
        print("Pause")

    def resume(self):
        print("resume")

    def next(self):
        print("next")

    def previous(self):
        print("previous")


class song(function_of_player):
    def __init__(self, name, duration, date_release, artist):
        self.name = name
        self.duration = duration
        self.date_release = date_release
        self.artist = artist

    def name(self, value):
        if isinstance(value, str) and len(value) >= 1:
            self.name = value
        else:
            raise ValueError("Name must be string. ")

    def duration(self, value):
        if isinstance(value, float) and value > 0:
            self.duration = value
        else:
            raise ValueError("Duration must be positive float number.")

    def date_release(self, value):
        if isinstance(value, datetime):
            self.date_release = value
        else:
            raise ValueError("Argument must be date.")

    def artist(self, value):
        if isinstance(value, str) and len(value) >= 1:
            self.artist = value
        else:
            raise ValueError("Genre must be string.")

