from __future__ import annotations


class Entity[TId]:
    def __init__(
        self,
        entity_id: TId,
    ) -> None:

        self._id = entity_id

    @property
    def id(
        self,
    ) -> TId:

        return self._id

    def __eq__(
        self,
        other: object,
    ) -> bool:

        if not isinstance(other, Entity):
            return False

        return type(self) is type(other) and self.id == other.id

    def __hash__(
        self,
    ) -> int:

        return hash(
            (
                type(self),
                self.id,
            )
        )
