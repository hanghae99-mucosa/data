# -*- coding: utf-8 -*-
from model.User import User
from faker import Faker
from collections import OrderedDict
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

class UserFaker():
    @logging_time
    def create_user_dataset(self, num):
        user_class_list = []

        # num개의 User 생성
        for i in range(1, num + 1):
            email = fake.unique.ascii_free_email()
            password = fake.sha256()
            # USER가 0, ADMIN 1
            role = fake.random_element(elements=OrderedDict([(0, 0.95), (1, 0.05)]))
            user = User(i, email, password, role)
            user_class_list.append(user)

        return user_class_list


if __name__ == "__main__":
    user_faker = UserFaker()
    user_class_list = user_faker.create_user_dataset(1000)

    user_cnt = 0
    admin_cnt = 0
    for i in range(1000):
        if user_class_list[i].role == 1:
            admin_cnt += 1
        if user_class_list[i].role == 0:
            user_cnt += 1

    print("일반 사용자 수 : ", user_cnt)
    print("셀러 수 : ", admin_cnt)