import asyncio
import inspect


class EventBus:
    def __init__(self):
        self._subscribers: dict[str, list[callable]] = {}

    def subscribe(self, event_type, handler: callable):
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []

        self._subscribers[event_type].append(handler)

    async def emit(self, event_type: str, *args, **kwargs):
        if event_type in self._subscribers:
            handlers = self._subscribers.get(event_type, [])
            tasks = []
            for handler in handlers:
                try:
                    if inspect.iscoroutinefunction(handler):
                        tasks.append(handler(*args, **kwargs))
                    else:
                        tasks.append(asyncio.to_thread(handler, *args, **kwargs))
                except TypeError as e:
                    print(f"[EventBus] handler error: {handler} - {e}")
                    raise e

            await asyncio.gather(*tasks)