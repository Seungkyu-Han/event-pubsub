from event_pubsub.event_bus import EventBus


class Subscriber:
    def __init__(self, event_bus: EventBus):
        self._event_bus = event_bus

    def subscribe(self, event_type: str):
        def decorator(handler: callable):
            self._event_bus.subscribe(event_type, handler)
            return handler
        return decorator