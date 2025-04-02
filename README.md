# Today's Fortune
### 🤗6. **운세 보기 + 오늘의 한마디 생성기**🤗

- **도메인**: 생년월일 관리 / 별자리 or 띠 기반 운세 / 오늘의 조언 / 기록
- **기능 예시**: 운세 텍스트 출력, “오늘의 한마디” 랜덤 출력
- ✅ 테스트 포인트: 운세 분류 함수, 랜덤 조언 생성기

### 1. 요구사항 명세서
## 1. 요구사항 명세서

| 요구사항 ID | 업무구분(대)   | 요구사항명       | 요구사항                                                                 | 중요도 | 난이도 | 기능 유형  |
|-------------|----------------|------------------|--------------------------------------------------------------------------|--------|--------|-------------|
| req-001     | 운세&nbsp;사이트 | 사용자 입력      | 사용자의 생년/월/일/출생시간/성별을<br>입력한다.                         | 상     | 중     | 인터페이스 |
| req-002     | 운세&nbsp;사이트 | 인터페이스 출력  | 사이트에서 입력받은 데이터를 바탕으로<br>운세 내용을 파트별로 크롤링한다. | 상     | 중     | 인터페이스 |


##  화면 정의서 - 초기화면

![image](https://github.com/user-attachments/assets/1ec8ccfc-21a4-436f-ba28-7f4fbe03ddf0)


###  페이지 구성 예시

![image](https://github.com/user-attachments/assets/911e84d8-cf41-43ee-8eb5-4454f5a505ef)


### 3. 테스트 계획서

| 테스트 ID  | 테스트 대분류 | 테스트 항목           | 테스트 세부내용                                         | 예상 결과                                                    | 실제 결과                                |
|------------|----------------|------------------------|----------------------------------------------------------|---------------------------------------------------------------|------------------------------------------|
| test-01    | 인터페&nbsp;이스     | 사용자 입&nbsp;력 및 출력    | 사용자의 생년/월/일/출생 시간/성별을 입력한다            | 한 줄 운세, 총운, 재물운, 애정운, 건강운의 운세 결과가 출력됨 | 한 줄 운세, 총운, 재물운, 애정운, 건강운의 운세 결과가 출력됐다 |


### 4. 결과
