from typing import Any, get_args, get_origin


class Reflection:
    """
    Reflection helpers for messaging.
    """

    @staticmethod
    def find_generic_base(
        cls: type,
        generic_type: type,
    ) -> tuple[type, tuple[Any, ...]] | None:
        """
        Finds the generic specialization of a base class.
        """

        for current in cls.__mro__:
            for base in getattr(
                current,
                "__orig_bases__",
                (),
            ):
                origin = get_origin(base)

                if origin is generic_type:
                    return (
                        origin,
                        get_args(base),
                    )

        return None
