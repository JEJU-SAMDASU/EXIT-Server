

# API 명세서 
자세한 내용은 [Notion](https://www.notion.so/API-cd1e4a5a5c6945ae9afe140d006c2a3a)참고
## User

### User - Client (신청자)

- POST `/auth/client/sign-up/` - `client`회원가입
- POST `/auth/client/login/` - `client`로그인

### User - Counselor (상담자)

- POST `/auth/counselor/sign-up/` - `counselor`회원가입
- POST `/auth/counselor/login/` - `counselor`로그인

### User - 유저 조회

- GET `/auth/counselor/` - 단일
- GET `/auth/counselors/` - List

### User - uid로 상담사의 가능 시간 조회

- GET `/auth/able-time/{uid}`

-----

## Reservation

- POST `/reservation/` - 예약 생성
- GET `/auth/able-time/`-  예약 확인 - 본인 `uid`와 일치하는 예약 목록
- DELETE `/reservation` - 예약 삭제

-----

## Search Category

- GET `/search/category` - 카테고리 검색

## video-chat

[리모트몬스터 단순 통화 앱](https://vinylrich.github.io/remon-devguide-quickstart/simplevideocall-tutorial.html)

## just-chat

> 사용법

- 각 url 하나씩 채팅하여 1:1채팅

GET `192.168.0.11/junwoo`
room1
GET `192.168.0.11/junsang`
room2
