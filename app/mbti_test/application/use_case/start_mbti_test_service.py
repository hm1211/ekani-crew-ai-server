import uuid
from datetime import datetime

from app.mbti_test.application.port.input.start_mbti_test_use_case import (
    StartMBTITestUseCase,
    StartMBTITestCommand,
    StartMBTITestResponse,
)
from app.mbti_test.application.port.output.mbti_test_session_repository import MBTITestSessionRepositoryPort
from app.mbti_test.infrastructure.service.human_question_provider import HumanQuestionProvider
from app.mbti_test.domain.mbti_test_session import MBTITestSession, TestStatus
from app.mbti_test.domain.mbti_message import MBTIMessage, MessageRole, MessageSource


class StartMBTITestService(StartMBTITestUseCase):
    def __init__(
        self,
        mbti_test_session_repository: MBTITestSessionRepositoryPort,
        human_question_provider: HumanQuestionProvider,
    ):
        self._mbti_test_session_repository = mbti_test_session_repository
        self._human_question_provider = human_question_provider

    def execute(self, command: StartMBTITestCommand) -> StartMBTITestResponse:
        # 1. 차원별 3개씩 랜덤 선택 (총 12개)
        selected_questions = self._human_question_provider.select_random_questions()

        # 2. 첫 번째 질문 생성
        first_question = MBTIMessage(
            role=MessageRole.ASSISTANT,
            content=selected_questions[0],
            source=MessageSource.HUMAN,
        )

        # 3. 세션 생성 (선택된 질문 저장)
        session = MBTITestSession(
            id=uuid.uuid4(),
            user_id=command.user_id,
            test_type=command.test_type,
            status=TestStatus.IN_PROGRESS,
            created_at=datetime.now(),
            questions=[first_question.content],  # 질문 히스토리
            selected_human_questions=selected_questions,  # 랜덤 선택된 12개 질문
        )

        self._mbti_test_session_repository.save(session)

        return StartMBTITestResponse(
            session=session,
            first_question=first_question,
        )