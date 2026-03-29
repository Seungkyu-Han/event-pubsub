import pytest
from unittest.mock import AsyncMock

from event_pubsub import Publisher


@pytest.mark.asyncio
async def test_publisher_publishes_event_correctly():
    # given
    mock_event_bus = AsyncMock()
    publisher = Publisher(event_bus=mock_event_bus)

    # when
    test_event_type = "test_event"
    test_data = {"email": "trust1204@gmailc.com"}

    await publisher.publish(test_event_type, test_data)

    # then
    mock_event_bus.emit.assert_called_once()

    mock_event_bus.emit.assert_called_with(test_event_type, test_data)
