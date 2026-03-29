import asyncio
import inspect


class EventBus:
    """
    A simple in-memory Event Bus for Python applications.

    Features:
    - Supports both synchronous and asynchronous handlers
    - Executes all handlers concurrently
    - Fail-fast behavior: raises an exception if any handler fails
    - Allows multiple subscribers per event type

    Usage:
        event_bus = EventBus()

        # subscribe handlers
        event_bus.subscribe("my_event", async_handler)
        event_bus.subscribe("my_event", sync_handler)

        # emit event
        await event_bus.emit("my_event", arg1, arg2)
    """

    def __init__(self):
        self._subscribers: dict[str, list[callable]] = {}

    def subscribe(self, event_type: str, handler: callable):
        """
        Subscribe a handler to a specific event type.

        Args:
            event_type (str): Name of the event.
            handler (callable): Function or coroutine to call when the event is emitted.
        """
        # Initialize list if this event_type has no subscribers yet
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []

        # Append the handler to the subscriber list (order is preserved)
        self._subscribers[event_type].append(handler)

    async def emit(self, event_type: str, *args, **kwargs):
        """
        Emit an event and call all registered handlers concurrently.

        Args:
            event_type (str): The event to emit.
            *args, **kwargs: Arguments to pass to the handlers.

        Raises:
            TypeError: If a handler cannot accept the given arguments.
        """
        # Only proceed if there are subscribers for this event
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