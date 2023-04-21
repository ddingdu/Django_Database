* DB 설계를 활용한 REST API 설계
DRF(Django Rest Framework) 를 활용한 API Server 제작

< 학습한 내용 >
- 단일 모델의 data 를 Serialize 하여 JSON 으로 변환
- API를 구축하고 만들기 위한 플랫폼인 postman 을 활용해서 단일 리뷰를 수정 및 삭제 하고 리뷰를 생성했습니다.

< 어려 웠던 부분 >
- serializer 를 생성 하면서 개수가 늘어나자 헷갈렸습니다. 실행해 보면서 확인하고, 모델 별로 나눠서 영역을 구분해 두었습니다.
- 댓글을 생성하는 POST 형식이 익숙하지 않아서 연습이 필요할 것 같습니다.

< 새로 배운 것들 >
- 모델 생성시 json 파일을 참고하면서 작성하면 loaddata 오류를 방지할 수 있다는 것을 알게 되었습니다. (json 파일과 fields 이름 일치 시키기)
- 단일 객체 인스턴스 대신 QuerySet 또는 객체 목록을 serialize 하려면 many=True를 작성한다고 배웠는데 역참조 해서 단일 객체를 serialize 할 때는 many=True를 빼고 read_only=True 만 넣어야 한다는 것을 배웠습니다.

< 느낀 점 >
- ModelSerializer 클래스를 반복해서 생성하며 편리함을 느꼈습니다.
- 오류를 찾아내고 수정해서 원하는 결과를 반환하는 과정에서 성장하는 것을 느꼈습니다.
