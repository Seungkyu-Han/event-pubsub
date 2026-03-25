from event_pubsub.event_bus import EventBus


class Publisher:
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus

    async def publish(self, event_type: str, data: any):
        await self.event_bus.emit(event_type, data)