from abc import abstractmethod, ABC
from .util import event_list, search_event_list

class EventBase(ABC):

    def __init__(self, chat_id: int, massage_id: int, event_id: str, prev_event_ids: list[str], message_text: str, buttons: list[str]):
        self.chat_id = chat_id
        self.message_id = massage_id
        self.event_id = event_id
        self.prev_event_ids = prev_event_ids
        self.message_text = message_text
        self.current_profile = Profile.load_profile(chat_id)
        self._sign_into_event_list(prev_event_ids,event_id)

    def _sign_into_event_list(self,prev_event_ids: list[str], event_id: str):
        """this method will sign into the event list"""

        for prev_event_id in prev_event_ids:
            event_list[prev_event_id].append({event_id: self})

    def create_virtual_keyboard(self, buttons: list[str]):  # TODO add right type for return object
        """This method calls the keyboard creation and returns a virtual keyboard object"""
        pass

    def _save_profile(current_profile, chat_id):
        Profile.save(current_profile,chat_id)

    def _get_next_events(self) -> list[{str: object}]:
        """searches all events for next events"""
        search_event_list(self.event_id, event_list)

    @abstractmethod
    def is_available(self, profile) -> bool:
        """This method check if all prerequisite for this event are meet"""
        pass


