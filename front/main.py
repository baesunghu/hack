import requests


def get_distance1(loc1, loc2):
    REST_API_KEY = "ddbb9ea580dea5d8d53c406f5d5ed23a"

    # 장소 검색 API로 역 이름(키워드) -> 좌표 변환 함수
    def get_coordinates_from_place(query):
        url = "https://dapi.kakao.com/v2/local/search/keyword.json"
        headers = {"Authorization": f"KakaoAK {REST_API_KEY}"}
        if not query.endswith("역"):
            query += "역"
        params = {"query": query}  # 역 이름 + '역' 추가해서 검색 정확도 향상

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        documents = data.get("documents", [])
        if not documents:
            return None

        doc = documents[0]  # 첫번째 결과 사용
        return {
            "address": doc.get("place_name"),
            "longitude": float(doc.get("x")),
            "latitude": float(doc.get("y"))
        }

    # 길찾기 API는 기존과 동일
    def get_route_distance(origin_coord, destination_coord):
        url = "https://apis-navi.kakaomobility.com/v1/directions"
        headers = {
            "Authorization": f"KakaoAK {REST_API_KEY}"
        }
        params = {
            "origin": f"{origin_coord['longitude']},{origin_coord['latitude']}",
            "destination": f"{destination_coord['longitude']},{destination_coord['latitude']}",
            "summary": "true",
            "priority": "RECOMMEND",
            "car_fuel": "GASOLINE",
            "car_hipass": "false",
            "alternatives": "false",
            "road_details": "false"
        }

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data['routes'][0]['summary']['distance']

    start_coord = get_coordinates_from_place(loc1)
    if not start_coord:
        print(f"출발지 '{loc1}' 좌표를 찾을 수 없습니다.")
        raise ValueError()

    end_coord = get_coordinates_from_place(loc2)
    if not end_coord:
        print(f"도착지 '{loc2}' 좌표를 찾을 수 없습니다.")
        raise ValueError()

    print(
        f"출발지: {start_coord['address']}, 경도: {start_coord['longitude']}, 위도: {start_coord['latitude']}")
    print(
        f"도착지: {end_coord['address']}, 경도: {end_coord['longitude']}, 위도: {end_coord['latitude']}")

    try:
        distance = get_route_distance(start_coord, end_coord)
        print(f"전체 거리: {distance} m")
        return distance
    except Exception as e:
        print("길찾기 API 호출 중 오류가 발생했습니다:", e)
        return -1
