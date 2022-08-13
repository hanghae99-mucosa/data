# -*- coding: utf-8 -*-
from table.User import User
from faker import Faker
from faker.providers import DynamicProvider

fake = Faker('ko_KR')

def create_user_dataset(num):

    user_class_list = []

    user_role_provider = DynamicProvider(
        provider_name="set_user_role",
        elements=["ADMIN", "USER"],
    )

    # 동적 프로바이더 추가
    fake.add_provider(user_role_provider)

    # num개의 User 생성
    for i in range(1, num + 1):
        email = fake.unique.ascii_free_email()
        password = fake.password()
        role = fake.set_user_role()
        user = User(i,email, password, role)
        user_class_list.append(user)

    return user_class_list

if __name__ == "__main__":
    user_class_list = create_user_dataset(100)

    for i in range(100):
        print(user_class_list[i])