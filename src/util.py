def search_event_list(event_id: str, event_list) -> list[{str: EventBase}]:
    event = event_list.get(event_id)
    if event is not None:
        return event
    else:
        None

event_list = {} # is a dict with event_id as key and a dict of event_id as key and event objects as value
