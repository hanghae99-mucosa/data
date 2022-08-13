from faker import Faker
import faker_commerce

fake = Faker('ko_KR')
fake.add_provider(faker_commerce.Provider)


# for _ in range(50):
#     reivew_avg = round(fake.pyfloat(min_value=0, max_value=5), 1)
#     if (reivew_avg < 1):
#         reivew_avg = 0
#     print(reivew_avg)

for i in range(10000):
    print(i)
    print(fake.unique.ecommerce_name())