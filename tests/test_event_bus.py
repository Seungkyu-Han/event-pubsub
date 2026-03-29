from unittest.mock import Mock

import pytest

from event_pubsub import EventBus


def test_event_bus_create_correctly():
    # then
    EventBus()


def test_event_bus_subscribe_correctly():
    # given
    test_handler = lambda x: ...
    test_event_type = 'event_type'

    # when
    event_bus = EventBus()

    # then
    event_bus.subscribe(test_event_type, test_handler)


@pytest.mark.asyncio
async def test_event_bus_emit_correctly():
    # given
    event_bus = EventBus()
    test_result: list[str] = []
    test_message = "hello"

    async def test_handler(array: list[str], data: str):
        array.append(data)

    event_bus.subscribe("test_event", test_handler)

    # when
    await event_bus.emit("test_event", test_result, test_message)

    # then
    assert test_result == [test_message]


@pytest.mark.asyncio
async def test_event_bus_emit_sync_func_correctly():
    # given
    event_bus = EventBus()
    test_result: list[str] = []
    test_message = "hello"

    def test_handler(array: list[str], data: str):
        array.append(data)

    event_bus.subscribe("test_event", test_handler)

    # when
    await event_bus.emit("test_event", test_result, test_message)

    # then
    assert test_result == [test_message]


@pytest.mark.asyncio
async def test_event_bus_emit_incorrectly_cause_invalid_args():
    # given
    event_bus = EventBus()
    test_result: list[str] = []
    test_message = "hello"

    async def handler(array: list[str], data: str, age: int):
        array.append(data)
        array.append(str(age))

    event_bus.subscribe("test_event", handler)
    await event_bus.emit("test_event", test_result, "hello", 123)

    assert test_result == [test_message, str(123)]

    # when
    with pytest.raises(TypeError):
        await event_bus.emit("test_event", test_result, test_message)

@pytest.mark.asyncio
async def test_subscribe_existing_event():
    event_bus = EventBus()

    def handler(data):
        pass

    event_bus.subscribe("test", handler)
    event_bus.subscribe("test", handler)

    assert len(event_bus._subscribers["test"]) == 2

@pytest.mark.asyncio
async def test_emit_event_without_subscribers():
    event_bus = EventBus()

    await event_bus.emit("no_event", "data")