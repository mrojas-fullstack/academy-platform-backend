from __future__ import annotations

from abc import ABC, abstractmethod

from app.modules.auth.application.dto import GoogleIdentity


class GoogleIdentityVerifier(ABC):
    @abstractmethod
    async def verify(
        self,
        credential: str,
    ) -> GoogleIdentity: ...
