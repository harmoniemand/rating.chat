from abc import abstractmethod, ABC
import os
from profile.profile import Profile
import importlib
import inspect


class EventBase(ABC):
    def __init__(self, chat_id: int, massage_id: int, event_id: str, prev_event_ids,
                 message_text: str, buttons):
        self.chat_id = chat_id
        self.message_id = massage_id
        self.event_id = event_id
        self.prev_event_ids = prev_event_ids
        self.message_text = message_text
        self.current_profile = Profile.load(chat_id)
        self._sign_into_event_list(prev_event_ids, event_id)

    def _sign_into_event_list(self, prev_event_ids, event_id: str):
        """this method will sign into the event list"""
        print("d")
        # for prev_event_id in prev_event_ids:
        #    create_event_list()#[prev_event_id].append({event_id: self})

    def create_virtual_keyboard(self, buttons):  # TODO add right type for return object
        """This method calls the keyboard creation and returns a virtual keyboard object"""
        pass

    def _save_profile(current_profile, chat_id):
        Profile.save(current_profile, chat_id)

    def _get_next_events(self) -> list:
        """searches all events for next events"""
        #search_event_list(self.event_id, event_list)

    @abstractmethod
    def is_available(self, profile) -> bool:
        """This method check if all prerequisite for this event are meet"""
        pass


def create_event_list():
    event_classes = [str(x.split('.')[0]) for x in os.listdir(os.path.join(os.getcwd(), '..', 'events'))]

    events = []
    for e in event_classes:
        module = importlib.import_module('events.{}'.format(e))
        if hasattr(module, e) and inspect.isclass(getattr(module, e)):
            events.append(getattr(module, e))
    return events


if __name__ == '__main__':
    print(create_event_list())

'''
def search_event_list(event_id: str, event_list) -> list[{str: EventBase}]:
    event = event_list.get(event_id)
    if event is not None:
        return event
    else:
        None
'''