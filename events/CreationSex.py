from src.event import EventBase


class CreationSex(EventBase):
    def __init__(self, chat_id: int, massage_id: int, event_id: str, prev_event_ids: list,
                 message_text: str, buttons: list):
        super().__init__(self, chat_id, massage_id, event_id, prev_event_ids,
                         message_text, buttons)
        print("asdr")

    def is_available(self, profile):
        return True