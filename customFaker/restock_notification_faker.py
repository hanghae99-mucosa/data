from model.Restock_Notification import Restock_Notification
from faker import Faker
from faker.providers import DynamicProvider
from customFaker.user_faker import UserFaker
from customFaker.brand_faker import BrandFaker
from customFaker.category_faker import CategoryFaker
from customFaker.product_faker import ProductFaker
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

class RestockNotificationFaker():
    @logging_time
    def create_restock_notification_dataset(self, user_class_list, product_class_list, num):

        restock_notification_class_list = []

        # 동적 프로바이더 생성시 role이 USER인 User 클래스만 모아서 elements에 넣어주기
        user_class_list_role_USER = []
        for user_class in user_class_list:
            # USER : 0, ADMIN : 1
            if user_class.role == 0:
                user_class_list_role_USER.append(user_class)

        restock_user_id_provider = DynamicProvider(
            provider_name="set_user_in_restock",
            elements=user_class_list_role_USER,
        )
        fake.add_provider(restock_user_id_provider)

        # 동적 프로바이더 생성시 amount가 0인 Product 클래스만 모아서 elements에 넣어주기
        product_class_list_amount_0 = []
        for product_class in product_class_list:
            if product_class.amount == 0:
                product_class_list_amount_0.append(product_class)

        restock_product_id_provider = DynamicProvider(
            provider_name="set_product_in_restock",
            elements=product_class_list_amount_0,
        )
        fake.add_provider(restock_product_id_provider)

        for i in range(1, num + 1):
            user_class = fake.set_user_in_restock()
            user_id = user_class.user_id
            product_class = fake.set_product_in_restock()
            product_id = product_class.product_id
            alarm_flag = fake.boolean()

            restock_notification = Restock_Notification(i, user_id, product_id, alarm_flag)
            restock_notification_class_list.append(restock_notification)

        return restock_notification_class_list

if __name__ == "__main__":
    user_faker = UserFaker()
    user_class_list = user_faker.create_user_dataset(50)

    brand_faker = BrandFaker()
    brand_class_list = brand_faker.create_brand_dataset(user_class_list, 5000)

    category_faker = CategoryFaker()
    category_class_list = category_faker.create_catogory_dataset()

    product_faker = ProductFaker()
    product_class_list = product_faker.create_product_dataset(brand_class_list, category_class_list, 1000)

    restock_notification_faker = RestockNotificationFaker()
    restock_notification_class_list = restock_notification_faker.create_restock_notification_dataset(user_class_list, product_class_list, 100)

    for restock in restock_notification_class_list:
        print(restock)

    print(len(restock_notification_class_list))