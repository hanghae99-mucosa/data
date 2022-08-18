from faker import Faker
# import faker_commerce
from collections import OrderedDict
import datetime

fake = Faker('ko_KR')
# fake.add_provider(faker_commerce.Provider)

# 리퓨평점 테스트
# for _ in range(50):
#     reivew_avg = round(fake.pyfloat(min_value=0, max_value=5), 1)
#     if (reivew_avg < 1):
#         reivew_avg = 0
#     print(reivew_avg)

# faker_commerce 테스트
# for i in range(10000):
#     print(i)
#     print(fake.unique.ecommerce_name())

# iso8601 테스트
# KST = datetime.timezone(datetime.timedelta(hours=9))
# for _ in range(1000):
#     print(fake.date_time_between(start_date="-2y").isoformat("T", "auto"))

# ..?
# price_range = OrderedDict([
#     (100000, 0.6),
#     (1000000, 0.3),
#     (10000000, 0.1),
# ])
#
# fake = Faker(price_range)
#
# price = fake.pyint(min_value=1000, max_value=10000000, step=100)

# pricetag
# for _ in range(50):
#     print(fake.pricetag())

# Brand 명 테스트
elements_list = ['무', '신', '사', '베', '르', '사', '체', '빈', '폴', '라', '코', '스', '테', '타', '미', '힐', '피', '거', '올', '젠',
                 '나', '이', '키', '아', '디', '다', '스', '뉴', '발', '란', '스', '아', '식', '스', '발', '렌', '시', '아', '가', '구', '찌',
                 '자', '라', '에', '이', '치', '엔', '엠', '유', '니', '클', '로']
elements = list(set(elements_list))
print(len(elements))
print(len(elements_list))
random_list = []
for _ in range(10000):
    brand_name = "".join(fake.random_elements(elements=elements, unique=True, length=4))
    print(brand_name)
    random_list.append(brand_name)

random_list_set = list(set(random_list))

print("random_list_set : ", len(random_list_set))
print("random_list : ", len(random_list))


