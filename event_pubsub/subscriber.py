from event_pubsub.event_bus import EventBus


class Subscriber:
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus

    def subscribe(self, event_type: str):
        def decorator(handler: callable):
            self.event_bus.subscribe(event_type, handler)
            return handler
        return decorator