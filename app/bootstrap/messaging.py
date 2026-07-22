from app.core.container import Container
from app.core.messaging import MessageBus, MessageRegistry


def build_messaging(
    container: Container,
) -> tuple[MessageRegistry, MessageBus]:

    registry = MessageRegistry(container)

    bus = MessageBus(
        registry=registry
    )

    return registry, bus