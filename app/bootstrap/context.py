from dataclasses import dataclass

from app.core.container import Container
from app.core.messaging import MessageBus, MessageRegistry
from app.core.settings import Settings


@dataclass(frozen=True, slots=True)
class ApplicationContext:
    settings: Settings

    container: Container

    registry: MessageRegistry

    bus: MessageBus
