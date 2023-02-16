from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_property():
    response = client.get("/property/All/under")
    assert response.status_code == 200
    # assert response.status_code == 404


def test_info():
    response = client.get("/info/1")
    assert response.status_code == 200
    # assert response.status_code == 404
    result = response.json()
    assert result["homeNumber"] == 1


def test_apply():
    req_data = {
              "homeNumber": 1,
              "roomId": 2,
              "name": "Hong",
              "phone": "010-1111-1111",
              "email": "test@test.com",
              "apply_privacy": "Y",
              "startDate": "2023-02-16",
              "endDate": "2023-03-16"
            }
    response = client.put("/apply", json=req_data)
    assert response.status_code == 200
    result = response.json()
    assert result == req_data


def test_regHome():
    req_data = {
              "homeNumber": 0,
              "title": "동대문 교통의 중심지 장기 숙박 호텔",
              "contents": "동대문과 을지로4가역에서 도보 5분 거리에 위치한 역세권 호텔 입니다. 풍부한 관광 인프라와 생활 편의시설이 많은 지역으로 해외에서 잠시 입국하는 분들 또는 "
                          "여행으로 방문하기 좋습니다. 장기 숙박으로 지내기 좋은 호텔로 주 1회 하우스키핑이 제공되며, 유료 코인 세탁기를 사용할 수 있습니다. 무료로 제공되는 피트니스 "
                          "센터에서 언제든 건강 관리를 할 수 있습니다. 평소 식당과 배달을 자주 이용하고 집에서 자주 요리를 하지 않는 분들에게 추천하는 공간 입니다. 어렵게 집을 찾고 "
                          "가전, 침대, 침구를 구매하지 않고 다 준비된 쾌적한 호텔에서 보증금 없이 살아보세요.",
              "rooms": [
                {
                  "roomId": 1,
                  "roomName": "스탠다드 더블 시티뷰",
                  "deposit": 0,
                  "rent": 31,
                  "periodType": "week"
                },
                {
                  "roomId": 2,
                  "roomName": "디럭스트윈 시티뷰",
                  "deposit": 0,
                  "rent": 31,
                  "periodType": "week"
                }
              ],
              "options": [
                "피트니스", "공용세탁기", "공용건조기"
              ],
              "startDate": "2023-02-20",
              "location": "Seoul",
              "period": "under"
            }
    response = client.put("/reg", json=req_data)
    assert response.status_code == 200
    result = response.json()
    assert result == req_data
