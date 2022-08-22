# -*- coding: utf-8 -*-
from model.User import User
from faker import Faker
from collections import OrderedDict
import time
import bcrypt

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
            email = "test" + str(i) + "@test.test"
            print(email)
            password = bcrypt.hashpw("test123!".encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
            # USER가 0, ADMIN 1
            role = fake.random_element(elements=OrderedDict([(0, 0.95), (1, 0.05)]))
            user = User(i, email, password, role)
            user_class_list.append(user)

        return user_class_list


if __name__ == "__main__":
    print("user_faker 시작!")
    user_faker = UserFaker()
    user_class_list = user_faker.create_user_dataset(100)

    user_cnt = 0
    admin_cnt = 0
    for user_class in user_class_list:
        if user_class.role == 1:
            admin_cnt += 1
        if user_class.role == 0:
            user_cnt += 1

    print("일반 사용자 수 : ", user_cnt)
    print("셀러 수 : ", admin_cnt)