from event_base.event import EventBase


class CreationSex(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['hello', 'hello'], event_id="creation_sex",
                 message_text="hello", buttons=[{'text' : 'test', 'next_event_id' : 'creation_age'}])

    def is_available( profile):
        return True
