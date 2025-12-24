import uuid
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from app.mbti_test.application.port.input.start_mbti_test_use_case import StartMBTITestCommand
from app.mbti_test.application.use_case.start_mbti_test_service import StartMBTITestService
from app.mbti_test.domain.mbti_test_session import TestType
from app.auth.adapter.input.web.auth_dependency import get_current_user_id
from app.mbti_test.application.port.output.mbti_test_session_repository import MBTITestSessionRepositoryPort
from app.mbti_test.application.port.output.question_provider_port import QuestionProviderPort
from app.mbti_test.infrastructure.repository.in_memory_mbti_test_session_repository import InMemoryMBTITestSessionRepository
from app.mbti_test.infrastructure.service.in_memory_question_provider import InMemoryQuestionProvider

mbti_router = APIRouter()

def get_session_repository() -> MBTITestSessionRepositoryPort:
    return InMemoryMBTITestSessionRepository()

def get_question_provider() -> QuestionProviderPort:
    return InMemoryQuestionProvider()

@mbti_router.post("/start")
async def start_mbti_test(
    test_type: TestType,
    user_id: str = Depends(get_current_user_id),
    session_repository: MBTITestSessionRepositoryPort = Depends(get_session_repository),
    question_provider: QuestionProviderPort = Depends(get_question_provider)
):
    use_case = StartMBTITestService(session_repository, question_provider)
    command = StartMBTITestCommand(user_id=uuid.UUID(user_id), test_type=test_type)
    result = use_case.execute(command)

    return jsonable_encoder({"session": result.session, "first_question": result.first_question})
