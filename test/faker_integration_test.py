from customFaker.user_faker import UserFaker
from customFaker.brand_faker import BrandFaker
from customFaker.category_faker import CategoryFaker
from customFaker.product_faker import ProductFaker
from customFaker.order_faker import OrderFaker
from customFaker.restock_notification_faker import RestockNotificationFaker

if __name__ == "__main__":
    # User 50명 생성
    user_faker = UserFaker()
    user_class_list = user_faker.create_user_dataset(50)

    # Brand 100개 생성
    brand_faker = BrandFaker()
    brand_class_list = brand_faker.create_brand_dataset(user_class_list, 100)

    # Category 생성
    category_faker = CategoryFaker()
    category_class_list = category_faker.create_catogory_dataset()

    # Product 1000개 생성
    product_faker = ProductFaker()
    product_class_list = product_faker.create_product_dataset(brand_class_list, category_class_list, 1000)

    # Order 100개 생성
    order_faker = OrderFaker()
    order_class_list = order_faker.create_order_dataset(user_class_list, product_class_list, 100)

    # Restock_Notification 100개 생성
    restock_notification_faker = RestockNotificationFaker()
    restock_notification_class_list = restock_notification_faker.create_restock_notification_dataset(user_class_list, product_class_list, 100)

    for product in product_class_list:
        print(product)
