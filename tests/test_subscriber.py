from unittest.mock import Mock
from event_pubsub.subscriber import Subscriber


def test_subscribe_registers_handler_and_returns_it():
    # given
    event_bus = Mock()
    subscriber = Subscriber(event_bus)

    def handler():
        ...

    # when
    returned_handler = subscriber.subscribe("test_event")(handler)

    # then
    event_bus.subscribe.assert_called_once_with("test_event", handler)
    assert returned_handler is handler