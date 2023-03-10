# homeapi

## 과제개요
유연한 주거 부동산 임대 서비스 셀* 서비스의 as-is API를 설계 및 구성하였다.

## 사용 기술
- Python 3.11.2
- Fastapi 0.92.0
- Pymongo 4.3.3
- Uvicorn 0.20.0
- Pytest 7.2.1 
- Pycharm-community 2022.3.2
- MongoDB 6.0.4
- MongoDB Compass 1.35.0  

## 구현 기능
### 1. 매물리스트 조회 API
#### GET /property/{location}/{preiod}
    Parameters : 
    - location : 지역 (All, Seoul, Gyeonggi, Incheon, Chungcheong, Gangwon, Jeolla, Busan, Jeju)
    - period : under / over (90일 미만, 이상)
    - date : 기준 입주일

    Response (http code 200 sample) :
                [
                  {
                    "homeNumber": 1,
                    "title": "동대문 교통의 중심지 장기 숙박 호텔",
                    "contents": "동대문과 을지로4가역에서 도보 5분 거리에 위치한 역세권 호텔 입니다. 풍부한 관광 인프라와 생활 편의시설이 많은 지역으로 해외에서 잠시 입국하는 분들 또는 여행으로 방문하기 좋습니다.장기 숙박으로 지내기 좋은 호텔로 주 1회 하우스키핑이 제공되며, 유료 코인 세탁기를 사용할 수 있습니다. 무료로 제공되는 피트니스 센터에서 언제든 건강 관리를 할 수 있습니다.평소 식당과 배달을 자주 이용하고 집에서 자주 요리를 하지 않는 분들에게 추천하는 공간 입니다. 어렵게 집을 찾고 가전, 침대, 침구를 구매하지 않고 다 준비된 쾌적한 호텔에서 보증금 없이 살아보세요.",
                    "rooms": [
                      {
                        "roomId": 1,
                        "roomName": "스탠다드 더블 시티뷰",
                        "deposit": 0,
                        "rent": 31,
                        "periodType": "week"
                      },
                      {
                        "roomId": 1,
                        "roomName": "디럭스 트윈 시티뷰",
                        "deposit": 0,
                        "rent": 31,
                        "periodType": "week"
                      }
                    ],
                    "options": [
                      "피트니스",
                      "공용세탁기",
                      "공용건조기"
                    ],
                    "startDate": "2023-02-15",
                    "location": "Seoul",
                    "period": "under"
                  }
                ]
### 2. 매물 조회 API
#### GET /info/{homeNumber}
    Parameters
    - homeNumber : 매물번호

    Response (http code 200 sample) :
                {
                  "homeNumber": 1,
                  "title": "동대문 교통의 중심지 장기 숙박 호텔",
                  "contents": "동대문과 을지로4가역에서 도보 5분 거리에 위치한 역세권 호텔 입니다. 풍부한 관광 인프라와 생활 편의시설이 많은 지역으로 해외에서 잠시 입국하는 분들 또는 여행으로 방문하기 좋습니다.장기 숙박으로 지내기 좋은 호텔로 주 1회 하우스키핑이 제공되며, 유료 코인 세탁기를 사용할 수 있습니다. 무료로 제공되는 피트니스 센터에서 언제든 건강 관리를 할 수 있습니다.평소 식당과 배달을 자주 이용하고 집에서 자주 요리를 하지 않는 분들에게 추천하는 공간 입니다. 어렵게 집을 찾고 가전, 침대, 침구를 구매하지 않고 다 준비된 쾌적한 호텔에서 보증금 없이 살아보세요.",
                  "rooms": [
                    {
                      "roomId": 1,
                      "roomName": "스탠다드 더블 시티뷰",
                      "deposit": 0,
                      "rent": 31,
                      "periodType": "week"
                    },
                    {
                      "roomId": 1,
                      "roomName": "디럭스 트윈 시티뷰",
                      "deposit": 0,
                      "rent": 31,
                      "periodType": "week"
                    }
                  ],
                  "options": [
                    "피트니스",
                    "공용세탁기",
                    "공용건조기"
                  ],
                  "startDate": "2023-02-15",
                  "location": "Seoul",
                  "period": "under"
                }
### 3. 입주 문의 신청 API
#### PUT /apply
    Example value : 
            {
              "homeNumber": 1,
              "roomId": 2,
              "name": "Hong",
              "phone": "010-1111-1111",
              "email": "test@test.com",
              "apply_privacy": "Y",
              "startDate": "2023-02-16",
              "endDate": "2023-03-16"
            }
### 4. 매물 등록 API
#### PUT /reg
    Example value : 
            {
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

## MongoDB 구조
    Database Name : home
    
    Connection info : pymonggo MongoClient, localhost:27017

    Collection : 
        - apply : 입주 문의 신청 collection
        - home : 매물 리스트 Collection 
    
## 사전과제
    1. 셀립
       코오롱의 커먼타운 등에 비해 호텔이나 레지던스 등 고급 주거유형이 많은 점이 강남 등에서 서비스 중인 
       에피소드와 가장 경쟁하고 있는 주거 서비스라고 생각한다.

    2. 셀립의 모바일 웹 as-is 의 서비스를 토대로 현 기능을 분석하여 구성하였다.
       매물리스트 조회 API
       매물 조회 API
       입주 문의 신청 API
       매물 등록 API

    3. 현재의 주거 서비스들은 고정된 계약이 아닌 플렉서블한 임대기간과 다양한 서비스, 고급화 등으로 유연한 임대방식이라
       내세우고 있지만 계약부터 입주신청 등의 과정은 전혀 유연하지 않으며 결국엔 옛날 방식대로 진행하게 된다.
       은행에 가지 않고 휴대폰으로 모든 금융서비스를 이용하는 현재의 시대처럼 결국 주거 서비스의 계약 및 입주도 본인인증이나
       신분증 촬영 등으로 신분을 확인하고 비대면 신청으로 이루어 질 수 있을 것이다. 
       ( 물론 개인정보의 이용 및 관련 법안 등 규제에 따라 다를 수 있다. )
       그리고 서비스의 이용으로 발생되는 비용 지불은 현재보다 더욱 다양하고 편리한 결제수단으로 지불 가능하게 될 것이다.(복합결제, 정기결제)
       유연하지 않은 매물 상담 및 계약 절차를 FastApi 같은 생산성 높은 기술로 매물에 대한 정보를 신속하게 제공하고 계약 절차 또한 본인인증 서비스 등을 도입하여
       비대면으로 유연하게 진행할 수 있도록 기여하고 싶다. 
