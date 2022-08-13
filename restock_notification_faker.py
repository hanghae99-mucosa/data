from table.Restock_Notification import Restock_Notification
from faker import Faker
from faker.providers import DynamicProvider
import user_faker
import product_faker
import brand_faker
import category_faker

fake = Faker('ko_KR')

def create_restock_notification_dataset(user_class_list, product_class_list, num):

    restock_notification_class_list = []

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
        alarm_flag = fake.boolean()

        restock_notification = Restock_Notification(i, user_id, product_id, alarm_flag)
        restock_notification_class_list.append(restock_notification)

    return restock_notification_class_list

if __name__ == "__main__":
    
    user_class_list = user_faker.create_user_dataset(50)

    brand_class_list = brand_faker.create_brand_dataset(user_class_list, 100)

    categroy_class_list = category_faker.create_catogory_dataset()

    product_class_list = product_faker.create_product_dataset(brand_class_list, categroy_class_list, 1000)

    restock_notification_class_list = create_restock_notification_dataset(user_class_list, product_class_list, 100)

    for restock in restock_notification_class_list:
        print(restock)

    print(len(restock_notification_class_list))