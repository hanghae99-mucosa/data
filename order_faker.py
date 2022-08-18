from table.Order import Order
from faker import Faker
from faker.providers import DynamicProvider
import user_faker
import product_faker
import brand_faker
import category_faker
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
def create_order_dataset(user_class_list, product_class_list, num):
    order_class_list = []

    order_user_id_provider = DynamicProvider(
        provider_name="set_user_in_order",
        elements=user_class_list,
    )

    fake.add_provider(order_user_id_provider)

    order_product_id_provider = DynamicProvider(
        provider_name="set_product_in_order",
        elements=product_class_list,
    )

    fake.add_provider(order_product_id_provider)

    for i in range(1, num + 1):
        user_class = fake.set_user_in_order()
        user_id = user_class.user_id
        product_class = fake.set_product_in_order()
        product_id = product_class.product_id
        amount = fake.pyint(min_value=1, max_value=10)
        product_price = product_class.price
        total_price = amount * product_price
        created_at = fake.date_time_between(start_date="-2y").isoformat("T", "auto")

        order = Order(i, user_id, product_id, amount, total_price, created_at)
        order_class_list.append(order)

    return order_class_list


if __name__ == "__main__":

    user_class_list = user_faker.create_user_dataset(50)

    brand_class_list = brand_faker.create_brand_dataset(user_class_list, 100)

    category_class_list = category_faker.create_catogory_dataset()

    product_class_list = product_faker.create_product_dataset(brand_class_list, category_class_list, 1000)

    order_class_list = create_order_dataset(user_class_list, product_class_list, 100)

    for order in order_class_list:
        print(order)

    print(len(order_class_list))
