# -*- coding: utf-8 -*-
from table.Brand import Brand
from faker import Faker
from faker.providers import DynamicProvider
import user_faker
import time

fake = Faker('ko_KR')

def logging_time(original_fn):
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = original_fn(*args, **kwargs)
        end_time = time.time()
        print("WorkingTime[{}]: {} sec".format(original_fn.__name__, end_time-start_time))
        return result
    return wrapper_fn

@logging_time
def create_brand_dataset(user_class_list, num):

    brand_class_list = []

    user_class_list_role_ADMIN = []
    for user_class in user_class_list:
        # USER : 0, ADMIN : 1
        if user_class.role == 1:
            user_class_list_role_ADMIN.append(user_class)

    # User와 Brand의 맵핑 관계 -> user_class_list를 elements에 할당
    brand_user_id_provider = DynamicProvider(
        provider_name="set_user_id_in_brand",
        elements=user_class_list_role_ADMIN,
    )
    # 동적 프로바이더 등록
    fake.add_provider(brand_user_id_provider)

    # brand_name 리스트 생성
    elements_list = ['무', '신', '사', '베', '르', '사', '체', '빈', '폴', '라', '코', '스', '테', '타', '미', '힐', '피', '거', '올', '젠',
                     '나', '이', '키', '아', '디', '다', '스', '뉴', '발', '란', '스', '아', '식', '스', '발', '렌', '시', '아', '가', '구', '찌',
                     '자', '라', '에', '이', '치', '엔', '엠', '유', '니', '클', '로']
    elements = list(set(elements_list))

    random_list = []
    for _ in range(10000):
        brand_name = "".join(fake.random_elements(elements=elements, unique=True, length=4))
        random_list.append(brand_name)

    brand_name_list = list(set(random_list))

    for i in range(1, num + 1):
        if len(brand_name_list) < i:
            print("더이상 brand name이 없습니다.")
        name = brand_name_list[i-1]

        user = fake.set_user_id_in_brand()
        user_id = user.user_id

        brand = Brand(i, name, user_id)
        brand_class_list.append(brand)

    return brand_class_list

if __name__ == "__main__":
    
    user_class_list = user_faker.create_user_dataset(50)

    user_class_list_role_ADMIN = []
    for user_class in user_class_list:
        # USER : 0, ADMIN : 1
        if user_class.role == 1:
            print(user_class)
            user_class_list_role_ADMIN.append(user_class)


    brand_class_list = create_brand_dataset(user_class_list, 1000)

    for brand in brand_class_list:
        print(brand)

    print(len(brand_class_list))