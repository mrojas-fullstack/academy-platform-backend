from app.core.container import Container
from app.core.messaging import MessageBus, MessageRegistry


def build_messaging(
    container: Container,
) -> tuple[MessageRegistry, MessageBus]:

    registry = MessageRegistry()

    bus = MessageBus(
        registry=registry,
        container=container,
    )

    return registry, bus
