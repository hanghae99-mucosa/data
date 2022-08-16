# -*- coding: utf-8 -*-
from table.Brand import Brand
from faker import Faker
from faker.providers import DynamicProvider
import user_faker

fake = Faker('ko_KR')

def create_brand_dataset(user_class_list, num):

    brand_class_list = []

    # User와 Brand의 맵핑 관계 -> user_class_list를 elements에 할당
    brand_user_id_provider = DynamicProvider(
        provider_name="set_user_id_in_brand",
        elements=user_class_list,
    )
    
    # 동적 프로바이더 등록
    fake.add_provider(brand_user_id_provider)


    # num개의 Brand 생성
    i = 1
    cnt = 0
    while True:
        if cnt == num:
            break
        user = fake.set_user_id_in_brand()
        # ADMIN : 1
        if(user.role == 1):
            user_id = user.user_id
            name = fake.unique.name()
            brand = Brand(i, name, user_id)
            brand_class_list.append(brand)
            cnt += 1
            i += 1

    return brand_class_list


if __name__ == "__main__":
    
    user_class_list = user_faker.create_user_dataset(50)

    brand_class_list = create_brand_dataset(user_class_list, 100)

    for brand in brand_class_list:
        print(brand)

    print(len(brand_class_list))