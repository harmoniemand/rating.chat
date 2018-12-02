from event_base.event import EventBase


class CreationAge(EventBase):
    def __init__(self, chat_id: int):
        event_id = "creation_age"
        super().__init__(chat_id=chat_id, prev_event_ids=["creation_user_name"], event_id=event_id , buttons=[{'text' :'18-24', 'next_event_id': 'creation_sex'}],
                         message_text="hello")

    def is_available(profile):
        return True

    def test(self):
        print("hey")