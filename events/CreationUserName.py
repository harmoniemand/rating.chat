from event_base.event import EventBase


class CreationUserName(EventBase):
    def __init__(self, chat_id: int):
        super().__init__(chat_id=chat_id, prev_event_ids=['start'], event_id="creation_user_name",
                         message_text="Choose a name", buttons=[{'text': 'Kai', 'next_event_id': 'creation_age'},
                                                                {'text' : 'Martin', 'next_event_id': 'creation_age'},
                                                                {'text' : 'Joni', 'next_event_id' : 'creation_age'}])

    def is_available(self, profile):
        return True
