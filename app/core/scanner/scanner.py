import pkgutil

from .loader import ModuleLoader
from .reflection import Reflection


class Scanner:
    def scan(
        self,
        package: str,
    ) -> list[type]:

        handlers: list[type] = []

        root = ModuleLoader.load(package)

        for _, module_name, _ in pkgutil.walk_packages(
            root.__path__,
            root.__name__ + ".",
        ):
            module = ModuleLoader.load(module_name)

            for cls in Reflection.get_classes(module):
                if Reflection.is_handler(cls):
                    handlers.append(cls)

        return handlers
