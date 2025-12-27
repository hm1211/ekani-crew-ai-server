from abc import ABC, abstractmethod
from typing import Optional
from enum import Enum


class MatchState(Enum):
    """User matching state"""
    IDLE = "idle"           # Not in queue, not matched
    QUEUED = "queued"       # In matching queue, waiting for match
    MATCHED = "matched"     # Matched with someone, waiting to connect to chat
    CHATTING = "chatting"   # Connected to chat room


class UserMatchState:
    """User match state data"""
    def __init__(
        self,
        user_id: str,
        state: MatchState,
        mbti: Optional[str] = None,
        room_id: Optional[str] = None,
        partner_id: Optional[str] = None
    ):
        self.user_id = user_id
        self.state = state
        self.mbti = mbti
        self.room_id = room_id
        self.partner_id = partner_id


class MatchStatePort(ABC):
    """
    Port for tracking user match states
    """

    @abstractmethod
    async def get_state(self, user_id: str) -> Optional[UserMatchState]:
        """Get user's current match state"""
        pass

    @abstractmethod
    async def set_queued(self, user_id: str, mbti: str) -> None:
        """Mark user as queued for matching"""
        pass

    @abstractmethod
    async def set_matched(
        self,
        user_id: str,
        mbti: str,
        room_id: str,
        partner_id: str,
        expire_seconds: int = 60
    ) -> None:
        """
        Mark user as matched.
        State expires after expire_seconds if user doesn't connect to chat.
        """
        pass

    @abstractmethod
    async def set_chatting(self, user_id: str, room_id: str) -> None:
        """Mark user as connected to chat"""
        pass

    @abstractmethod
    async def clear_state(self, user_id: str) -> None:
        """Clear user's match state (back to idle)"""
        pass

    @abstractmethod
    async def is_available_for_match(self, user_id: str) -> bool:
        """Check if user can be matched (idle or queued only)"""
        pass
