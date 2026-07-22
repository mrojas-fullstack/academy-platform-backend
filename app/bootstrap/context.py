from dataclasses import dataclass

from app.core.settings import Settings
from app.core.container import Container
from app.core.messaging import MessageBus, MessageRegistry


@dataclass(frozen=True, slots=True)
class ApplicationContext:

    settings: Settings

    container: Container

    registry: MessageRegistry

    bus: MessageBus