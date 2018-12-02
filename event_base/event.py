from abc import abstractmethod, ABC
from profile.profile import Profile
from telegram import InlineKeyboardButton


class EventBase(ABC):
    def __init__(self, chat_id: int, event_id: str, prev_event_ids,
                 message_text: str, buttons):

        self.chat_id = chat_id
        self.event_id = event_id
        self.buttons = buttons
        self.prev_event_ids = prev_event_ids
        self.message_text = message_text
        self.current_profile = None

    def create_virtual_keyboard(self):
        """This method calls the keyboard creation and returns a virtual keyboard object"""
        button_list = []
        for e in self.buttons:
            next_event_id = e['next_event_id']
            next_event_id = next_event_id+';'+str(self.chat_id)
            button_list.append(InlineKeyboardButton(e['text'], callback_data=next_event_id))
        return button_list, self.message_text

    def _save_profile(self):
        Profile.save(self.current_profile, self.chat_id)

    def _get_profile(self):
        return Profile.load(self.chat_id)

    def _get_next_events(self) -> list:
        """searches all events for next events"""
        pass

    def _get_current_profile(self):
        self.current_profile = Profile.load(self.chat_id)

    @abstractmethod
    def is_available(self, profile) -> bool:
        """This method check if all prerequisite for this event are meet"""
        return True





'''
def search_event_list(event_id: str, event_list) -> list[{str: EventBase}]:
    event = event_list.get(event_id)
    if event is not None:
        return event
    else:
        None
'''