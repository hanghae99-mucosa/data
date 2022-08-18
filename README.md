# MUCOSA-DATA

## 프로젝트 설명
- MUCOSA 프로젝트에 필요한 더미데이터를 Faker패키지로 생성해 RDS에 적재하는 프로그램입니다.

## 프로그램 구조
![Mucosa-data](https://user-images.githubusercontent.com/47559613/185379525-78ca65c5-9584-4966-a5be-8d019dc518d1.jpg)


## 개발환경
- Python 3.6.5
- Faker 패키지
- Sqlalchemy 패키지

## 프로그램 폴더 설명
### 1. customFaker
- Faker 패키지를 통해 각각의 테이블에 맞게 더미 데이터를 생성하는 파일들이 들어있습니다.
- product_faker에서 사용되는 product_name_provider파일이 들어있습니다.

### 2. model
- customFaker로 생성한 더미 데이터를 적재하기 용이하도록 클래스와 시키기위한 테이블별 클래스 파일들이 들어있습니다.
- Sqlacodegen 패키지를 이용해 기존 DB 테이블 정보를 바탕으로 테이블 각각에 대한 ORM 모델 클래스를 생성한 models.py 파일이 들어있습니다.

### 3. test
- Faker 패키지의 기능들을 test하는 파일들이 있습니다.
- customFaker가 정상 작동하는지 확인하는 test 파일들이 있습니다.

## 프로그램 작동 흐름

### 1. main.py파일에서 생성해줄 데이터의 수를 입력한 뒤 터미널 창에 아래와 같이 입력합니다.
```shell
python main.py
```

### 2. UserFaker를 통해 사용자 더미 데이터가 생성되고 연결된 RDS에 데이터가 적재됩니다.
```shell
- user_id : 랜덤값 ❌, 1부터 증가
- emial : 이메일 관련 랜덤값 ⭕
- password : 비밀번호 관련 랜덤값 ❌
- role : USER, ADMIN 랜덤값 ⭕ (단, User 95% Admin 5% 비율) 
```

### 3. BrandFaker를 통해 브랜드 더미 데이터가 생성되고 연결된 RDS에 데이터가 적재됩니다.
```shell
- brand_id : 랜덤값 ❌, 1부터 증가
- name : 한글을 랜덤하게 조합한 랜덤값 ⭕
- user_id : 랜덤값 ❌, user 테이블에 있는 id 값이면서 role이 Admin인 경우!
```

### 4. CategoryFaker를 통해 카테고리 더미 데이터가 생성되고 연결된 RDS에 데이터가 적재됩니다.
```shell
- category_id : 랜덤값 ❌, 1부터 증가
- category : 랜덤값 ❌
- parent_cateogry : 랜덤값 ❌, category 테이블에서 상위 category에 해당하는 ID값 + 최상위 category일 때는 null값
```

### 5. ProductFaker를 통해 상품 더미 데이터가 생성되고 연결된 RDS에 데이터가 적재됩니다.
```shell
- product_id : 랜덤값 ❌, 1부터 증가
- brand_id : 랜덤값 ❌, 브랜드 테이블에 있는 id 값
- name : 옷 관련 랜덤값 ⭕
- thumbnail : 랜덤값 ❌, 저작권 없는 이미지 주소를 카테고리 값에 맞게 생성
- category_id : 랜덤값 ❌, 카테고리 테이블에 있는 id 값
- price : 1000원부터 10,000,000원까지 랜덤 값(단, 100원 단위 ex, 92,010원 ❌ 92,100원 ⭕) & 가격 구간별 비율 다르게 생성
- amount : 0개 ~ 999개 랜덤값 ⭕ (단, 알림기능을 위해 인위적으로 amount가 0인 값을 중간에 넣어서 생성할 것)
- review_num : 0개 ~ 50,000개 랜덤값 ⭕ (단, review_avg가 0점이라면 review_num도 0으로 초기화)
- review_avg : 0점 ~ 5점(0.1단위) 랜덤값 ⭕
```

### 6. OrderFaker를 통해 주문 더미 데이터가 생성되고 연결된 RDS에 데이터가 적재됩니다.
```shell
- order_id : 랜덤값 ❌, 1부터 증가
- user_id : 랜덤값 ❌, user 테이블에 있는 id 값
- product_id : 랜덤값 ❌, product 테이블에 있는 id 값
- amount : 1개 ~ 10개 랜덤값
- totalPrice : 랜덤값 ❌, product_id의 price의 값 * amount 값!
- createdAt : LocalDateTime 랜덤값 ⭕ (단, 최근 2년까지의 날짜로 생성)
```

### 6. RestockNotificationFaker를 통해 재고 알림 더미 데이터가 생성되고 연결된 RDS에 데이터가 적재됩니다.
```shell
- restock_id : 랜덤값 ❌, 1부터 증가
- user_id : 랜덤값 ❌, user 테이블에 있는 id 값
- product_id : 랜덤값 ❌, product 테이블에 있는 id 값
- alarm_flag : 랜덤값 ⭕, product_id의 amount값이 0일 경우에 False, True 랜덤값
```

### 7. 모든 데이터가 적재되면 종료합니다.
