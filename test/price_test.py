from faker import Faker
from collections import OrderedDict

fake = Faker('ko_KR')

max_value_100000_cnt = 0
max_value_500000_cnt = 0
max_value_1000000_cnt = 0
max_value_5000000_cnt = 0
max_value_10000000_cnt = 0

for i in range(1, 1000):
    # max value 확률 지정
    max_value = fake.random_element(
        elements=OrderedDict([
            ("100000", 0.7),
            ("500000", 0.2),
            ("1000000", 0.05),
            ("5000000", 0.03),
            ("10000000", 0.02)
        ])
    )
    if max_value == "100000":
        price = fake.pyint(min_value=1000, max_value=int(max_value), step=100)
        max_value_100000_cnt += 1
    if max_value == "500000":
        price = fake.pyint(min_value=100001, max_value=int(max_value), step=1000)
        max_value_500000_cnt += 1
    if max_value == "1000000":
        price = fake.pyint(min_value=500001, max_value=int(max_value), step=1000)
        max_value_1000000_cnt += 1
    if max_value == "5000000":
        price = fake.pyint(min_value=1000001, max_value=int(max_value), step=1000)
        max_value_5000000_cnt += 1
    if max_value == "10000000":
        price = fake.pyint(min_value=5000001, max_value=int(max_value), step=1000)
        max_value_10000000_cnt += 1

print("max_value_100000_cnt", max_value_100000_cnt)
print("max_value_500000_cnt", max_value_500000_cnt)
print("max_value_1000000_cnt", max_value_1000000_cnt)
print("max_value_5000000_cnt", max_value_5000000_cnt)
print("max_value_10000000_cnt", max_value_10000000_cnt)