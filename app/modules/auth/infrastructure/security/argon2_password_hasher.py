from argon2 import PasswordHasher as Argon2
from argon2.exceptions import VerificationError
from argon2.low_level import Type

from app.core.security import PasswordHasher


class Argon2PasswordHasher(PasswordHasher):
    def __init__(self) -> None:
        self._hasher = Argon2(
            time_cost=3,
            memory_cost=65536,
            parallelism=4,
            hash_len=32,
            salt_len=16,
            type=Type.ID,
        )

    def hash(self, password: str) -> str:
        return self._hasher.hash(password)

    def verify(
        self,
        password: str,
        hashed_password: str,
    ) -> bool:
        try:
            return self._hasher.verify(
                hashed_password,
                password,
            )
        except VerificationError:
            return False
