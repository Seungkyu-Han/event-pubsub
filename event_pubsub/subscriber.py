from event_pubsub.event_bus import EventBus


class Subscriber:
    """
    A simple subscriber class that registers event handlers to an EventBus.

    This class provides a convenient decorator-based interface for subscribing
    functions or coroutines to specific event types.

    Usage:
        event_bus = EventBus()
        subscriber = Subscriber(event_bus)

        # Using as a decorator for async handler
        @subscriber.subscribe("my_event")
        async def handle_my_event(data):
            print(data)

        # Using as a decorator for sync handler
        @subscriber.subscribe("my_event")
        def handle_sync_event(data):
            print(data)
    """

    def __init__(self, event_bus: EventBus):
        """
        Initialize the Subscriber with an EventBus instance.

        Args:
            event_bus (EventBus): The EventBus instance where handlers will be registered.
        """
        self._event_bus = event_bus

    def subscribe(self, event_type: str):
        """
        Returns a decorator that registers a function or coroutine as a handler
        for a specific event type.

        Args:
            event_type (str): The event type to subscribe to.

        Returns:
            decorator (callable): A decorator function that registers the handler.
        """
        def decorator(handler: callable):
            self._event_bus.subscribe(event_type, handler)
            return handler

        return decorator