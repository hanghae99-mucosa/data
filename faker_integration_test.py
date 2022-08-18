import user_faker
import category_faker
import brand_faker
import product_faker
import order_faker
import restock_notification_faker


if __name__ == "__main__":
    # User 50명 생성
    user_class_list = user_faker.create_user_dataset(50)

    # Brand 100개 생성
    brand_class_list = brand_faker.create_brand_dataset(user_class_list, 100)

    # Category 생성
    category_class_list = category_faker.create_catogory_dataset()

    # Product 1000개 생성
    product_class_list = product_faker.create_product_dataset(brand_class_list, category_class_list, 1000)

    # Order 100개 생성
    order_class_list = order_faker.create_order_dataset(user_class_list, product_class_list, 100)

    # Restock_Notification 100개 생성
    restock_notification_class_list = restock_notification_faker.create_restock_notification_dataset(user_class_list, product_class_list, 100)

    for product in product_class_list:
        print(product)
