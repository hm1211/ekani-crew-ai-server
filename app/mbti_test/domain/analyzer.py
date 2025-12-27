import re

DICTIONARY = {
    "EI": {
        "E": [
            {"word": "같이", "w": 5}, {"word": "사람", "w": 3}, {"word": "모임", "w": 5},
            {"word": "떠들", "w": 3}, {"word": "만나", "w": 4}, {"word": "친구들", "w": 5},
            {"word": "다같이", "w": 5}, {"word": "여럿이", "w": 5}, {"word": "파티", "w": 4},
            {"word": "술자리", "w": 4}, {"word": "회식", "w": 4}, {"word": "번개", "w": 5},
            {"word": "나가", "w": 3}, {"word": "밖에", "w": 3}, {"word": "외출", "w": 3},
            {"word": "약속", "w": 4}, {"word": "만남", "w": 4}, {"word": "대화", "w": 3},
            {"word": "수다", "w": 5}, {"word": "톡", "w": 3}, {"word": "전화", "w": 3},
            {"word": "연락", "w": 3}, {"word": "놀", "w": 4}, {"word": "함께", "w": 4},
            {"word": "우리", "w": 3}, {"word": "다들", "w": 3}, {"word": "활발", "w": 4},
            {"word": "시끌", "w": 4}, {"word": "왁자지껄", "w": 5}, {"word": "떠들썩", "w": 5}
        ],
        "I": [
            {"word": "혼자", "w": 5}, {"word": "조용", "w": 4}, {"word": "집에", "w": 5},
            {"word": "생각", "w": 3}, {"word": "기빨려", "w": 5}, {"word": "이어폰", "w": 4},
            {"word": "집콕", "w": 5}, {"word": "방콕", "w": 5}, {"word": "쉬고", "w": 3},
            {"word": "충전", "w": 4}, {"word": "휴식", "w": 3}, {"word": "피곤", "w": 4},
            {"word": "귀찮", "w": 4}, {"word": "나만", "w": 4}, {"word": "혼자만", "w": 5},
            {"word": "고요", "w": 4}, {"word": "조용히", "w": 4}, {"word": "차분", "w": 4},
            {"word": "은둔", "w": 5}, {"word": "방구석", "w": 5}, {"word": "침대", "w": 3},
            {"word": "집순이", "w": 5}, {"word": "집돌이", "w": 5}, {"word": "인싸 아닌", "w": 5},
            {"word": "조용한", "w": 4}, {"word": "깊이", "w": 3}, {"word": "내면", "w": 4},
            {"word": "사색", "w": 4}, {"word": "명상", "w": 4}, {"word": "독서", "w": 3},
            # 구어체/줄임말 추가
            {"word": "힘들", "w": 4}, {"word": "힘듦", "w": 4}, {"word": "힘드노", "w": 4},
            {"word": "침묵", "w": 5}, {"word": "조용히있", "w": 5}, {"word": "가만", "w": 4},
            {"word": "짜져", "w": 5}, {"word": "누워", "w": 4}, {"word": "눕고싶", "w": 5},
            {"word": "집가", "w": 5}, {"word": "집에갈", "w": 5}, {"word": "집감", "w": 5},
            {"word": "각봄", "w": 4}, {"word": "집각", "w": 5}, {"word": "빠져나", "w": 4},
            {"word": "혼밥", "w": 5}, {"word": "혼술", "w": 5}, {"word": "혼영", "w": 5},
            {"word": "조용조용", "w": 4}, {"word": "숨어", "w": 4}, {"word": "숨고싶", "w": 5},
            {"word": "말안", "w": 4}, {"word": "안함", "w": 3}, {"word": "아웃사이더", "w": 5}
        ]
    },
    "SN": {
        "S": [
            {"word": "사실", "w": 5}, {"word": "현실", "w": 4}, {"word": "경험", "w": 4},
            {"word": "직접", "w": 3}, {"word": "구체적", "w": 5}, {"word": "팩트", "w": 3},
            {"word": "실제로", "w": 4}, {"word": "본", "w": 3}, {"word": "들은", "w": 3},
            {"word": "해봤", "w": 4}, {"word": "겪은", "w": 4}, {"word": "당장", "w": 4},
            {"word": "지금", "w": 3}, {"word": "현재", "w": 3}, {"word": "실질적", "w": 5},
            {"word": "실용적", "w": 5}, {"word": "효율적", "w": 4}, {"word": "구체적으로", "w": 5},
            {"word": "정확히", "w": 4}, {"word": "확실히", "w": 4}, {"word": "분명히", "w": 4},
            {"word": "증거", "w": 4}, {"word": "데이터", "w": 4}, {"word": "통계", "w": 4},
            {"word": "실전", "w": 4}, {"word": "실생활", "w": 4}, {"word": "실무", "w": 4},
            {"word": "현장", "w": 4}, {"word": "실체", "w": 4}, {"word": "명확", "w": 4},
            {"word": "세부", "w": 4}, {"word": "디테일", "w": 4}, {"word": "눈에 보이는", "w": 5},
            {"word": "만져본", "w": 4}, {"word": "경험상", "w": 5}, {"word": "과거에", "w": 3},
            # 구어체/줄임말 추가
            {"word": "존예", "w": 4}, {"word": "존잘", "w": 4}, {"word": "존멋", "w": 4},
            {"word": "이쁘", "w": 3}, {"word": "예쁘", "w": 3}, {"word": "예뻐", "w": 3},
            {"word": "살듯", "w": 4}, {"word": "사야", "w": 4}, {"word": "살거", "w": 4},
            {"word": "얼굴", "w": 4}, {"word": "머리", "w": 4}, {"word": "옷", "w": 3},
            {"word": "신발", "w": 3}, {"word": "가방", "w": 3}, {"word": "피부", "w": 3},
            {"word": "먼저", "w": 3}, {"word": "우선", "w": 3}, {"word": "가까운", "w": 4},
            {"word": "봤는데", "w": 4}, {"word": "보이", "w": 3}, {"word": "들리", "w": 3},
            {"word": "집부터", "w": 5}, {"word": "집사", "w": 5}, {"word": "차사", "w": 5},
            {"word": "실제", "w": 4}, {"word": "실물", "w": 4}, {"word": "ㄹㅇ", "w": 4},
            {"word": "리얼", "w": 4}, {"word": "진짜", "w": 3}, {"word": "찐", "w": 4}
        ],
        "N": [
            {"word": "의미", "w": 5}, {"word": "상상", "w": 5}, {"word": "미래", "w": 4},
            {"word": "가능성", "w": 5}, {"word": "만약에", "w": 5}, {"word": "비유", "w": 3},
            {"word": "추상", "w": 4}, {"word": "이론", "w": 4}, {"word": "개념", "w": 4},
            {"word": "아이디어", "w": 5}, {"word": "영감", "w": 5}, {"word": "직관", "w": 4},
            {"word": "느낌", "w": 3}, {"word": "뭔가", "w": 3}, {"word": "어쩌면", "w": 4},
            {"word": "나중에", "w": 3}, {"word": "언젠가", "w": 4}, {"word": "결국", "w": 3},
            {"word": "본질", "w": 5}, {"word": "심층", "w": 4}, {"word": "근본", "w": 4},
            {"word": "철학", "w": 5}, {"word": "깊은", "w": 4}, {"word": "숨은", "w": 4},
            {"word": "패턴", "w": 4}, {"word": "연결", "w": 4}, {"word": "관계", "w": 3},
            {"word": "상징", "w": 4}, {"word": "은유", "w": 4}, {"word": "창의", "w": 5},
            {"word": "혁신", "w": 5}, {"word": "비전", "w": 5}, {"word": "꿈", "w": 4},
            {"word": "이상", "w": 4}, {"word": "통찰", "w": 5}, {"word": "해석", "w": 4},
            {"word": "암시", "w": 4}, {"word": "함의", "w": 5}, {"word": "새로운", "w": 4}
        ]
    },
    "TF": {
        "T": [
            {"word": "이유", "w": 5}, {"word": "원인", "w": 5}, {"word": "논리", "w": 5},
            {"word": "분석", "w": 4}, {"word": "왜", "w": 5}, {"word": "해결", "w": 4},
            {"word": "보험", "w": 5}, {"word": "합리", "w": 5}, {"word": "효율", "w": 4},
            {"word": "객관", "w": 5}, {"word": "판단", "w": 4}, {"word": "평가", "w": 4},
            {"word": "기준", "w": 4}, {"word": "정확", "w": 4}, {"word": "사실", "w": 3},
            {"word": "증명", "w": 4}, {"word": "근거", "w": 5}, {"word": "타당", "w": 5},
            {"word": "논증", "w": 5}, {"word": "결론", "w": 4}, {"word": "추론", "w": 4},
            {"word": "인과", "w": 5}, {"word": "체계", "w": 4}, {"word": "구조", "w": 4},
            {"word": "시스템", "w": 4}, {"word": "방법", "w": 3}, {"word": "전략", "w": 4},
            {"word": "계획적", "w": 4}, {"word": "냉정", "w": 5}, {"word": "냉철", "w": 5},
            {"word": "이성", "w": 5}, {"word": "실리", "w": 4}, {"word": "득실", "w": 5},
            {"word": "손익", "w": 5}, {"word": "따져", "w": 5}, {"word": "계산", "w": 4},
            {"word": "어떻게", "w": 4}, {"word": "방식", "w": 3}, {"word": "수단", "w": 4},
            {"word": "절차", "w": 4}, {"word": "규칙", "w": 4}, {"word": "원리", "w": 4},
            {"word": "법칙", "w": 4}, {"word": "솔직히", "w": 3}, {"word": "어이없", "w": 4},
            {"word": "황당", "w": 4}, {"word": "뭔말", "w": 3}, {"word": "당연", "w": 4},
            {"word": "아니지", "w": 3}, {"word": "팩폭", "w": 5}, {"word": "직설", "w": 5},
            {"word": "퍽이나", "w": 4}, {"word": "웃기", "w": 3}, {"word": "말도안", "w": 4},
            {"word": "대신", "w": 3}, {"word": "해주", "w": 3}, {"word": "개선", "w": 5},
            {"word": "수정", "w": 4}, {"word": "육하원칙", "w": 5}, {"word": "따라", "w": 3},
            {"word": "비효율", "w": 5}, {"word": "최적", "w": 5}, {"word": "다르지않", "w": 4},
            {"word": "에따라", "w": 3},
            # 구어체/줄임말 추가
            {"word": "뭐가", "w": 4}, {"word": "뭔가", "w": 3}, {"word": "어캐", "w": 4},
            {"word": "반박", "w": 5}, {"word": "부들부들", "w": 5}, {"word": "논쟁", "w": 5},
            {"word": "이겼", "w": 4}, {"word": "졌", "w": 4}, {"word": "틀렸", "w": 4},
            {"word": "맞았", "w": 4}, {"word": "팩트체크", "w": 5}, {"word": "팩트", "w": 4},
            {"word": "웃긴게", "w": 4}, {"word": "왤케", "w": 4}, {"word": "왜냐", "w": 5},
            {"word": "힘드노", "w": 4}, {"word": "뭐노", "w": 4}, {"word": "어쩔", "w": 3},
            {"word": "지는건", "w": 4}, {"word": "못함", "w": 3}, {"word": "못해", "w": 3},
            {"word": "안됨", "w": 3}, {"word": "안돼", "w": 3}, {"word": "별론데", "w": 4},
            {"word": "솔까", "w": 4}, {"word": "솔직", "w": 4}, {"word": "직빵", "w": 4},
            {"word": "걍", "w": 2}, {"word": "그래서", "w": 3}, {"word": "그러니까", "w": 4}
        ],
        "F": [
            {"word": "기분", "w": 5}, {"word": "마음", "w": 5}, {"word": "공감", "w": 5},
            {"word": "서운", "w": 4}, {"word": "감정", "w": 5}, {"word": "속상", "w": 5},
            {"word": "어떡해", "w": 5}, {"word": "느낌", "w": 4}, {"word": "감성", "w": 5},
            {"word": "정서", "w": 4}, {"word": "위로", "w": 5}, {"word": "힐링", "w": 5},
            {"word": "따뜻", "w": 4}, {"word": "배려", "w": 5}, {"word": "존중", "w": 4},
            {"word": "이해", "w": 4}, {"word": "고민", "w": 4}, {"word": "걱정", "w": 4},
            {"word": "불안", "w": 4}, {"word": "슬픔", "w": 4}, {"word": "기쁨", "w": 3},
            {"word": "행복", "w": 3}, {"word": "사랑", "w": 4}, {"word": "좋아", "w": 3},
            {"word": "싫어", "w": 3}, {"word": "화나", "w": 4}, {"word": "짜증", "w": 4},
            {"word": "답답", "w": 4}, {"word": "억울", "w": 5}, {"word": "미안", "w": 4},
            {"word": "고마", "w": 4}, {"word": "감동", "w": 5}, {"word": "눈물", "w": 5},
            {"word": "울", "w": 4}, {"word": "아픔", "w": 4}, {"word": "상처", "w": 5},
            {"word": "치유", "w": 5}, {"word": "마음이", "w": 5}, {"word": "가슴", "w": 4},
            {"word": "심정", "w": 5}, {"word": "감정적", "w": 5}, {"word": "인간적", "w": 5},
            {"word": "따뜻한", "w": 5}, {"word": "공감해", "w": 5}, {"word": "위로해", "w": 5},
            {"word": "힘들", "w": 4}, {"word": "안쓰러", "w": 5}, {"word": "불쌍", "w": 4},
            {"word": "측은", "w": 5}, {"word": "기뻐", "w": 4}, {"word": "진심", "w": 4},
            {"word": "우울", "w": 5}, {"word": "힘내", "w": 5}, {"word": "괜찮", "w": 4},
            {"word": "응원", "w": 5}, {"word": "착하", "w": 3},
            # 구어체/줄임말 추가
            {"word": "본인이", "w": 5}, {"word": "좋으면", "w": 4}, {"word": "됐지", "w": 4},
            {"word": "본인맘", "w": 5}, {"word": "알아서", "w": 3}, {"word": "맘대로", "w": 4},
            {"word": "그래됐", "w": 4}, {"word": "어쩔수없", "w": 4}, {"word": "받아들", "w": 4},
            {"word": "이해해", "w": 5}, {"word": "이해함", "w": 5}, {"word": "그럴수", "w": 4},
            {"word": "ㅠㅠ", "w": 5}, {"word": "ㅜㅜ", "w": 5}, {"word": "ㅎㅎ", "w": 3},
            {"word": "ㅋㅋ", "w": 2}, {"word": "잘됐", "w": 4}, {"word": "잘했", "w": 4},
            {"word": "고생", "w": 4}, {"word": "수고", "w": 4}, {"word": "안아줘", "w": 5},
            {"word": "토닥", "w": 5}, {"word": "ㅇㅋ", "w": 3}, {"word": "오키", "w": 3},
            {"word": "ㅇㅇ", "w": 2}, {"word": "알겠", "w": 3}, {"word": "화이팅", "w": 5},
            {"word": "파이팅", "w": 5}, {"word": "존버", "w": 4}, {"word": "아쉽", "w": 4}
        ]
    },
    "JP": {
        "J": [
            {"word": "계획", "w": 5}, {"word": "정리", "w": 4}, {"word": "미리", "w": 5},
            {"word": "확정", "w": 4}, {"word": "리스트", "w": 5}, {"word": "예약", "w": 4},
            {"word": "스케줄", "w": 5}, {"word": "일정", "w": 5}, {"word": "체크", "w": 4},
            {"word": "준비", "w": 4}, {"word": "사전", "w": 4}, {"word": "미리미리", "w": 5},
            {"word": "예정", "w": 4}, {"word": "정해", "w": 4}, {"word": "결정", "w": 4},
            {"word": "확실", "w": 4}, {"word": "정확", "w": 3}, {"word": "명확", "w": 3},
            {"word": "체계", "w": 4}, {"word": "순서", "w": 4}, {"word": "단계", "w": 4},
            {"word": "규칙", "w": 4}, {"word": "원칙", "w": 4}, {"word": "기준", "w": 3},
            {"word": "정돈", "w": 4}, {"word": "정렬", "w": 4}, {"word": "분류", "w": 4},
            {"word": "마감", "w": 4}, {"word": "데드라인", "w": 5}, {"word": "기한", "w": 4},
            {"word": "시간 맞춰", "w": 5}, {"word": "약속 시간", "w": 5}, {"word": "정시", "w": 4},
            {"word": "체크리스트", "w": 5}, {"word": "투두", "w": 5}, {"word": "할 일", "w": 4},
            {"word": "완료", "w": 3}, {"word": "마무리", "w": 4}, {"word": "끝내", "w": 3},
            {"word": "깔끔", "w": 4}, {"word": "정확히", "w": 4}, {"word": "틀림없이", "w": 4},
            # 구어체/줄임말 추가
            {"word": "어디로", "w": 4}, {"word": "갈건데", "w": 4}, {"word": "정해야", "w": 5},
            {"word": "계획짜", "w": 5}, {"word": "짜야지", "w": 5}, {"word": "어캐할지", "w": 5},
            {"word": "만나기전", "w": 5}, {"word": "전에", "w": 3}, {"word": "해야지", "w": 4},
            {"word": "해야함", "w": 4}, {"word": "해야해", "w": 4}, {"word": "해야됨", "w": 4},
            {"word": "정하고", "w": 4}, {"word": "정한", "w": 4}, {"word": "알아보", "w": 4},
            {"word": "찾아보", "w": 4}, {"word": "검색", "w": 4}, {"word": "확인", "w": 4},
            {"word": "일주일", "w": 3}, {"word": "먼저정", "w": 5}, {"word": "미리정", "w": 5}
        ],
        "P": [
            {"word": "즉흥", "w": 5}, {"word": "그때", "w": 4}, {"word": "유연", "w": 4},
            {"word": "대충", "w": 4}, {"word": "일단", "w": 5}, {"word": "상황 봐서", "w": 4},
            {"word": "나중에", "w": 4}, {"word": "천천히", "w": 3}, {"word": "여유", "w": 4},
            {"word": "자유", "w": 4}, {"word": "편한", "w": 3}, {"word": "느긋", "w": 4},
            {"word": "막", "w": 4}, {"word": "아무", "w": 3}, {"word": "뭐든", "w": 4},
            {"word": "그냥", "w": 3}, {"word": "그렇게", "w": 2}, {"word": "알아서", "w": 4},
            {"word": "흐름", "w": 4}, {"word": "타이밍", "w": 4}, {"word": "순간", "w": 3},
            {"word": "융통", "w": 5}, {"word": "임기응변", "w": 5}, {"word": "애드립", "w": 5},
            {"word": "변화", "w": 3}, {"word": "적응", "w": 4}, {"word": "조절", "w": 3},
            {"word": "바꿔", "w": 3}, {"word": "다시", "w": 2}, {"word": "또", "w": 2},
            {"word": "나중", "w": 4}, {"word": "미루", "w": 5}, {"word": "일단은", "w": 5},
            {"word": "가다가", "w": 4}, {"word": "보면서", "w": 4}, {"word": "지금은", "w": 3},
            {"word": "당장", "w": 3}, {"word": "급하게", "w": 3}, {"word": "여유롭게", "w": 4},
            {"word": "막상", "w": 4}, {"word": "생각나면", "w": 4}, {"word": "끌리면", "w": 4},
            {"word": "하고 싶을 때", "w": 5}, {"word": "기분 내킬 때", "w": 5},
            # 구어체/줄임말 추가
            {"word": "시켰으니", "w": 4}, {"word": "먹긴해", "w": 4}, {"word": "별로여도", "w": 4},
            {"word": "자연스럽", "w": 5}, {"word": "흘러가", "w": 5}, {"word": "기다려", "w": 4},
            {"word": "봐야지", "w": 4}, {"word": "해봐야", "w": 4}, {"word": "머", "w": 3},
            {"word": "뭐", "w": 3}, {"word": "별로", "w": 3}, {"word": "상관없", "w": 4},
            {"word": "됐어", "w": 3}, {"word": "ㅇㅋ", "w": 3}, {"word": "괜찮", "w": 3},
            {"word": "어쩔수없", "w": 4}, {"word": "어쩔", "w": 3}, {"word": "몰라", "w": 4},
            {"word": "글쎄", "w": 4}, {"word": "모르겠", "w": 4}, {"word": "됐지", "w": 4}
        ]
    }
}

DESCRIPTIONS = {
    "ISTP": {"title": "만능 재주꾼", "traits": ["#냉철함", "#해결사"], "desc": "사고 현장에서도 수리비부터 계산할 쿨한 해결사군요!"},
    "ENFP": {"title": "재기발랄한 활동가", "traits": ["#에너지", "#인싸"], "desc": "세상을 즐거움으로 채우는 당신은 자유로운 영혼입니다!"},
}


def get_dimension_for_question(question_index: int) -> str:
    """질문 인덱스에 따른 MBTI 차원 반환"""
    if question_index < 3:
        return "EI"
    elif question_index < 6:
        return "SN"
    elif question_index < 9:
        return "TF"
    else:
        return "JP"


def analyze_single_answer(answer: str, dimension: str) -> dict:
    """단일 답변을 분석하여 MBTI 점수 반환"""
    scores = {k: 0 for k in "EISNTFJP"}

    # 키워드 매칭
    if dimension in DICTIONARY:
        for trait, keywords in DICTIONARY[dimension].items():
            for k in keywords:
                if k["word"] in answer:
                    scores[trait] += k["w"]

    # 스타일 보정 적용
    apply_style_correction(answer, dimension, scores)

    # 해당 차원의 양쪽 점수 추출
    if dimension == "EI":
        side = "E" if scores["E"] >= scores["I"] else "I"
        score = max(scores["E"], scores["I"])
    elif dimension == "SN":
        side = "S" if scores["S"] >= scores["N"] else "N"
        score = max(scores["S"], scores["N"])
    elif dimension == "TF":
        side = "T" if scores["T"] >= scores["F"] else "F"
        score = max(scores["T"], scores["F"])
    else:  # JP
        side = "J" if scores["J"] >= scores["P"] else "P"
        score = max(scores["J"], scores["P"])

    return {
        "scores": scores,
        "side": side,
        "score": score,
    }


def apply_style_correction(ans: str, dim: str, scores: dict):
    ans_len = len(ans)

    if dim == "EI":
        if ans_len > 50:
            scores["E"] += 1
        elif ans_len < 20:
            scores["I"] += 1

    if dim == "SN":
        abstract_words = ["것", "거", "뭔가", "느낌", "같은", "듯"]
        abstract_count = sum(w in ans for w in abstract_words)
        if abstract_count >= 2:
            scores["N"] += 1

        concrete_words = ["번", "개", "명", "시", "분", "회"]
        concrete_count = sum(w in ans for w in concrete_words)
        if concrete_count >= 2:
            scores["S"] += 1

    if dim == "TF":
        question_indicators = ans.count("?") + ans.count("어떻게") + ans.count("왜")
        if question_indicators >= 2:
            scores["T"] += 1

        exclamations = ["!", "ㅠ", "ㅜ", "ㅎ", "ㅋ", "♥", "❤", "😢", "😭", "💕"]
        exclamation_count = sum(ans.count(e) for e in exclamations)
        if exclamation_count >= 3:
            scores["F"] += 2
        elif exclamation_count >= 1:
            scores["F"] += 1

    if dim == "JP":
        decisive_words = ["해야", "할 거야", "할게", "예정", "반드시", "꼭"]
        if any(word in ans for word in decisive_words):
            scores["J"] += 1

        uncertain_words = ["아마", "글쎄", "모르겠", "될 듯", "일단", "어쩌면"]
        if sum(word in ans for word in uncertain_words) >= 1:
            scores["P"] += 1


def calculate_partial_mbti(answers: list):
    scores = {k: 0 for k in "EISNTFJP"}

    for i, ans in enumerate(answers):
        dim = ""
        if i < 3:
            dim = "EI"
        elif i < 6:
            dim = "SN"
        elif i < 9:
            dim = "TF"
        elif i < 12:
            dim = "JP"

        if not dim:
            continue

        keyword_matched = False

        for trait, keywords in DICTIONARY[dim].items():
            for k in keywords:
                if isinstance(ans, str) and k["word"] in ans:
                    scores[trait] += k["w"]
                    keyword_matched = True

        if isinstance(ans, str):
            if dim == "SN":
                if re.search(r"만약에|~라면|어쩌면|언젠가|미래에|가능성|상상", ans):
                    scores["N"] += 3
                    keyword_matched = True
                if re.search(r"실제로|경험상|직접|해봤|본 적|현실적으로", ans):
                    scores["S"] += 3
                    keyword_matched = True

            if dim == "TF":
                if re.search(r"왜 그런지|이유가 뭐야|논리적|합리적|따져보면", ans):
                    scores["T"] += 4
                    keyword_matched = True
                if re.search(r"기분이|마음이|감정적|공감|위로|속상|서운", ans):
                    scores["F"] += 4
                    keyword_matched = True

            if dim == "JP":
                if re.search(r"계획|미리|스케줄|예약|정해|체크리스트", ans):
                    scores["J"] += 3
                    keyword_matched = True
                if re.search(r"즉흥|일단|상황 봐서|그때 가서|나중에|대충", ans):
                    scores["P"] += 3
                    keyword_matched = True

        if not keyword_matched and isinstance(ans, str):
            apply_style_correction(ans, dim, scores)

    partial_mbti = ""

    if answers and len(answers) > 0:
        if len(answers) >= 3:
            partial_mbti += ("E" if scores["E"] >= scores["I"] else "I")
        else:
            partial_mbti += "X"

        if len(answers) >= 6:
            partial_mbti += ("S" if scores["S"] >= scores["N"] else "N")
        else:
            partial_mbti += "X"

        if len(answers) >= 9:
            partial_mbti += ("T" if scores["T"] >= scores["F"] else "F")
        else:
            partial_mbti += "X"

        if len(answers) >= 12:
            partial_mbti += ("J" if scores["J"] >= scores["P"] else "P")
        else:
            partial_mbti += "X"
    else:
        partial_mbti = "XXXX"

    return {"mbti": partial_mbti, "scores": scores}


def run_analysis(answers: list):
    scores = {k: 0 for k in "EISNTFJP"}

    for i, ans in enumerate(answers):
        dim = "EI" if i < 3 else "SN" if i < 6 else "TF" if i < 9 else "JP"

        keyword_matched = False

        for trait, keywords in DICTIONARY[dim].items():
            for k in keywords:
                if k["word"] in ans:
                    scores[trait] += k["w"]
                    keyword_matched = True

        if dim == "SN":
            if re.search(r"만약에|~라면|어쩌면|언젠가|미래에|가능성|상상", ans):
                scores["N"] += 3
                keyword_matched = True
            if re.search(r"실제로|경험상|직접|해봤|본 적|현실적으로", ans):
                scores["S"] += 3
                keyword_matched = True

        if dim == "TF":
            if re.search(r"왜 그런지|이유가 뭐야|논리적|합리적|따져보면", ans):
                scores["T"] += 4
                keyword_matched = True
            if re.search(r"기분이|마음이|감정적|공감|위로|속상|서운", ans):
                scores["F"] += 4
                keyword_matched = True

        if dim == "JP":
            if re.search(r"계획|미리|스케줄|예약|정해|체크리스트", ans):
                scores["J"] += 3
                keyword_matched = True
            if re.search(r"즉흥|일단|상황 봐서|그때 가서|나중에|대충", ans):
                scores["P"] += 3
                keyword_matched = True

        if not keyword_matched:
            apply_style_correction(ans, dim, scores)

    res_mbti = (
            ("E" if scores["E"] >= scores["I"] else "I") +
            ("S" if scores["S"] >= scores["N"] else "N") +
            ("T" if scores["T"] >= scores["F"] else "F") +
            ("J" if scores["J"] >= scores["P"] else "P")
    )

    def get_conf(a, b):
        return round((abs(a - b) / (a + b + 0.1)) * 100, 1)

    confidence = {
        "EI": get_conf(scores["E"], scores["I"]),
        "SN": get_conf(scores["S"], scores["N"]),
        "TF": get_conf(scores["T"], scores["F"]),
        "JP": get_conf(scores["J"], scores["P"])
    }

    return res_mbti, scores, confidence