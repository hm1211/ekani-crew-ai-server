from app.mbti_test.application.port.output.question_provider_port import QuestionProviderPort
from app.mbti_test.domain.mbti_message import MBTIMessage, MessageRole, MessageSource


class InMemoryQuestionProvider(QuestionProviderPort):
    def get_initial_question(self) -> MBTIMessage:
        return MBTIMessage(
            role=MessageRole.ASSISTANT,
            content="MBTI 검사를 시작합니다. 첫 번째 질문입니다: 새로운 사람들을 만나는 것을 즐기시나요?",
            source=MessageSource.HUMAN,
        )
