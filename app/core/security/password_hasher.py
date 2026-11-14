from abc import ABC, abstractmethod


class PasswordHasher(ABC):
    """
    Contract for password hashing implementations.
    """

    @abstractmethod
    def hash(
        self,
        password: str,
    ) -> str:
        """
        Hashes a plain text password.
        """
        raise NotImplementedError

    @abstractmethod
    def verify(
        self,
        password: str,
        hashed_password: str,
    ) -> bool:
        """
        Verifies a plain password against its hash.
        """
        raise NotImplementedError
