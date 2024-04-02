import pytest
from models.events import EventUpdate

#definition fixture
"""
픽스처는 재사용 할수 있는 함수로, 
필요한 데이터를 반환하기 위해서 쓴다.

픽스처 데코레이터는 인수를 선택적으로 받ㅇ르 수 있다. 예를 들어 scope 인수는 픽스처 함수의 유효 범위를 지정할 대 사용된다. 여기서는 두 가지 scope를 사용한다. 
session: 테스트 전체 세션동안 해당 함수가 유효하다.
module: 테스트 파일이 실행된 후 특정 함수에서만 유효하다.  
"""
@pytest.fixture
def event() -> EventUpdate:
    return EventUpdate(
        title="FastAPI Book Launch",
        image="https://packt.com/fastapi.png",
        description="We will be discussing the contents of the FastAPI book in"
                    "this evvenrt.Ensure to come withe your own copy to win gifts!",
        tags=["python", "fastapi", "book", "launch"],
        location="Google Meet"
    )

def test_event_name(event: EventUpdate) -> None:
    assert event.title == "FastAPI Book Launch"
