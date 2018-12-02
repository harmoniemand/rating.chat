import importlib
import inspect
import os

def create_event_list(chat_id):
    event_classes = [str(x.split('.')[0]) for x in os.listdir(os.path.join(os.getcwd(), '..', 'events'))]

    events = {}
    for e in event_classes:
        module = importlib.import_module('events.{}'.format(e))
        if hasattr(module, e) and inspect.isclass(getattr(module, e)):
            event = getattr(module, e)(chat_id)
            events[event.event_id] = {'prev' : [] ,'class' : getattr(module, e)}
            for entry in event.prev_event_ids:
                events[event.event_id]['prev'].append(entry)
    return events
"""
if __name__ == '__main__':
    event_list = create_event_list()
    test = event_list[0]
    getattr()"""