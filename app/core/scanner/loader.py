import importlib
from types import ModuleType

from .exceptions import PackageNotFoundError


class ModuleLoader:
    @staticmethod
    def load(
        module_name: str,
    ) -> ModuleType:

        try:
            return importlib.import_module(module_name)

        except ModuleNotFoundError as ex:
            raise PackageNotFoundError(
                module_name,
            ) from ex
