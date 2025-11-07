import datetime

# 가짜 회의실 데이터
MEETING_ROOMS = [
    {"name": "A", "capacity": 6,  "available": True, "user": None},
    {"name": "B", "capacity": 10, "available": False, "user": "Leo"},
    {"name": "C", "capacity": 4,  "available": True, "user": None},
    {"name": "D", "capacity": 7,  "available": True, "user": None},
    {"name": "E", "capacity": 20, "available": True, "user": None},
    {"name": "F", "capacity": 4,  "available": True, "user": None},
]

def get_meeting_rooms():
    """현재 회의실 목록 조회"""
    return MEETING_ROOMS

def reserve_meeting_room(room_name: str, user_name: str = "Guest"):
    """회의실 예약 (mock)"""
    for room in MEETING_ROOMS:
        if room["name"].lower() == room_name.lower():
            if not room["available"]:
                return {"status": "fail", "message": f"{room_name}은 이미 예약됨"}
            room["available"] = False
            room["user"] = user_name
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            return {"status": "success", "message": f"{user_name}님이 {room_name} 회의실을 {time}에 예약 완료"}
    return {"status": "fail", "message": f"{room_name} 회의실을 찾을 수 없음"}


def cancel_meeting_room(room_name: str, user_name: str = "Guest"):
    return {"status": "fail", "message": f"아직 회의실 예약 취소 기능은 구현되어 있지 않습니다."}
