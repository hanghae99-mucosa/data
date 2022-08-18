import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import user_faker
import brand_faker
import category_faker
import order_faker
import product_faker
import restock_notification_faker
from models import User
from models import Brand
from models import Category
from models import Product
from models import Order
from models import RestockNotification
from dotenv import load_dotenv

load_dotenv()

host = os.environ.get("HOST")
port = os.environ.get("PORT")
username = os.environ.get("DB_USERNAME")
database = os.environ.get("DATABASE")
password = os.environ.get("PASSWORD")

DATABASE_PATH = 'mysql://{0}:{1}@{2}:{3}/{4}'.format(username, password, host, port, database)

if __name__ == "__main__":

    engine = create_engine(DATABASE_PATH, echo=False, future=True)

    Session = sessionmaker(engine)
    session = Session()

    #============== user table에 저장
    user_class_list = user_faker.create_user_dataset(200)
    for user_class in user_class_list:
        user = User()
        user.email = user_class.email
        user.password = user_class.password
        user.role = user_class.role
        session.add(user)
        session.commit()


    #============== brand table에 저장
    brand_class_list = brand_faker.create_brand_dataset(user_class_list, 100)
    for brand_class in brand_class_list:
        brand = Brand()
        brand.name = brand_class.name
        brand.user_id = brand_class.user_id
        session.add(brand)
        session.commit()


    #============== category table에 저장
    category_class_list = category_faker.create_catogory_dataset()
    for category_class in category_class_list:
        category = Category()
        category.category = category_class.category
        category.parent_category = category_class.parent_cateogory
        session.add(category)
        session.commit()


    #============== product table에 저장
    # Product 1000개 생성
    product_class_list = product_faker.create_product_dataset(brand_class_list, category_class_list, 1000)
    for product_class in product_class_list:
        product = Product()
        product.amount = product_class.amount
        product.name = product_class.name
        product.price = product_class.price
        product.review_avg = product_class.review_avg
        product.review_num = product_class.review_num
        product.thumbnail = product_class.thumbnail
        product.brand_id = product_class.brand_id
        product.category_id = product_class.category_id
        session.add(product)
        session.commit()


    #============== order table에 저장
    # Order 1000개 생성
    order_class_list = order_faker.create_order_dataset(user_class_list, product_class_list, 100)
    for order_class in order_class_list:
        order = Order()
        order.created_at = order_class.createdAt
        order.amount = order_class.amount
        order.total_price = order_class.totalPrice
        order.product_id = order_class.product_id
        order.user_id = order_class.user_id
        session.add(order)
        session.commit()


    #============== restock_notification table에 저장
    # Restock_Notification 100개 생성
    restock_notification_class_list = restock_notification_faker.create_restock_notification_dataset(user_class_list, product_class_list, 100)
    for restock_notification_class in restock_notification_class_list:
        restock_notification = RestockNotification()
        restock_notification.alarm_flag = restock_notification_class.alarm_flag
        restock_notification.product_id = restock_notification_class.product_id
        restock_notification.user_id = restock_notification_class.user_id
        session.add(restock_notification)
        session.commit()

    # session 종료
    session.close()