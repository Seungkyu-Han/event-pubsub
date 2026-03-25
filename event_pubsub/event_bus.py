import asyncio

class EventBus:
    def __init__(self):
        self._subscribers: dict[str, list[callable]] = {}

    def subscribe(self, event_type, handler: callable):
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []

        self._subscribers[event_type].append(handler)

    async def emit(self, event_type: str, data: any):
        if event_type in self._subscribers:
            tasks = [handler(data) for handler in self._subscribers[event_type]]
            await asyncio.gather(*tasks)