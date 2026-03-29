from event_pubsub.event_bus import EventBus


class Publisher:
    """
    A simple publisher class that emits events through an EventBus.

    This class acts as a convenient wrapper around EventBus for publishing events.

    Usage:
        event_bus = EventBus()
        publisher = Publisher(event_bus)

        # publish an event
        await publisher.publish("my_event", data)
    """

    def __init__(self, event_bus: EventBus):
        """
        Initialize the Publisher with an EventBus instance.

        Args:
            event_bus (EventBus): The EventBus instance used for emitting events.
        """
        self._event_bus = event_bus

    async def publish(self, event_type: str, data: any):
        """
        Publish an event with the given type and data.

        Args:
            event_type (str): The name/type of the event to emit.
            data (any): The payload or data to pass to all subscribers of this event.

        Notes:
            - This method delegates the actual emission to the underlying EventBus.
            - Both synchronous and asynchronous subscribers will be handled automatically.
        """
        await self._event_bus.emit(event_type, data)