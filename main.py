from customFaker.user_faker import UserFaker
from customFaker.brand_faker import BrandFaker
from customFaker.category_faker import CategoryFaker
from customFaker.product_faker import ProductFaker
from customFaker.order_faker import OrderFaker
from customFaker.restock_notification_faker import RestockNotificationFaker
from dotenv import load_dotenv
from model.models import User
from model.models import Brand
from model.models import Category
from model.models import Product
from model.models import Order
from model.models import RestockNotification
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import func
import pymysql
import time

pymysql.install_as_MySQLdb()
load_dotenv()

host = os.environ.get("HOST")
port = os.environ.get("PORT")
username = os.environ.get("DB_USERNAME")
database = os.environ.get("DATABASE")
password = os.environ.get("PASSWORD")

DATABASE_PATH = 'mysql://{0}:{1}@{2}:{3}/{4}'.format(username, password, host, port, database)

if __name__ == "__main__":

    engine = create_engine(DATABASE_PATH, echo=False, future=True, encoding="utf-8", pool_recycle=3600)

    Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    session = Session()

    # print("user_query 실행")
    # user_query_start = time.time()  # 시작 시간 저장
    # user_query = session.query(User).order_by(User.user_id)
    # user_class_list = user_query.all()
    # print("user_query time :", time.time() - user_query_start)  # 현재시각 - 시작시간 = 실행 시간

    # print("num_list 실행")
    # num_list_start = time.time()
    # num_list = [i for i in range(1, 4501277)]
    # print("num_list time :", time.time() - num_list_start)
    #
    # none_user_id_list = []
    # print("user_class_list for문 실행")
    # for_start = time.time()
    # for user_class in user_class_list:
    #     if user_class.user_id not in num_list:
    #         none_user_id_list.append(user_class.user_id)
    # print("user_class_list for문 time :", time.time() - for_start)


    # brand_query = session.query(Brand).order_by(Brand.brand_id)
    # brand_class_list = brand_query.all()
    #
    # category_query = session.query(Category).order_by(Category.category_id)
    # category_class_list = category_query.all()

    # try:
    #     print("product_query 실행")
    #     product_query_start = time.time()  # 시작 시간 저장
    #     product_query = session.query(Product).order_by(Product.product_id)
    #     product_id = product_query.get(1124564)
    #     print("product_id : ", product_id.product_id)
    #     print("product_query time :", time.time() - product_query_start)  # 현재시각 - 시작시간 = 실행 시간
    # except :
    #     print("예외 발생")

    # print("#====== user table에 저장 ======#")
    # # User 4,500,0000명 생성
    # for i in range(224):
    #     user_faker = UserFaker()
    #     # user_query = session.query(User).order_by(User.user_id)
    #     # start_time = time.time()
    #     user_cnt = session.query(func.count(User.user_id)).scalar()
    #     start = user_cnt + 1
    #     # print("time :", time.time() - start_time)  # 현재시각 - 시작시간 = 실행 시간
    #     user_class_list = user_faker.create_user_dataset(start, 5000)
    #     for user_class in user_class_list:
    #         user = User()
    #         user.email = user_class.email
    #         user.password = user_class.password
    #         user.role = user_class.role
    #         session.add(user)
    #     session.commit()
    #     print(i + 1, "번 째 저장완료!")

    # print("#====== brand table에 저장 ======#")
    # # Brand 5000개 생성
    # brand_faker = BrandFaker()
    # brand_class_list = brand_faker.create_brand_dataset(user_class_list, 1000)
    # for brand_class in brand_class_list:
    #     brand = Brand()
    #     brand.name = brand_class.name
    #     brand.user_id = brand_class.user_id
    #     session.add(brand)
    # session.commit()
    #
    #
    # print("#====== category table에 저장 ======#")
    # category_faker = CategoryFaker()
    # category_class_list = category_faker.create_catogory_dataset()
    # for category_class in category_class_list:
    #     category = Category()
    #     category.category = category_class.category
    #     category.parent_category = category_class.parent_category
    #     session.add(category)
    # session.commit()


    # print("#====== product table에 저장 ======#")
    # for i in range(1):
    #     # Product 1,000,000개 생성
    #     product_faker = ProductFaker()
    #     product_class_list = product_faker.create_product_dataset(brand_class_list, category_class_list, 10000)
    #     for product_class in product_class_list:
    #         product = Product()
    #         product.amount = product_class.amount
    #         product.name = product_class.name
    #         product.price = product_class.price
    #         product.review_avg = product_class.review_avg
    #         product.review_num = product_class.review_num
    #         product.thumbnail = product_class.thumbnail
    #         product.brand_id = product_class.brand_id
    #         product.category_id = product_class.category_id
    #         session.add(product)
    #     session.commit()
    #     print(i + 1, "번 째 저장완료!")


    print("#====== order table에 저장 ======#")
    # Order 35,000,000개 생성
    user_class_list = []
    product_class_list = []
    for i in range(43):
        order_faker = OrderFaker()
        print("order_class_list 실행")
        order_class_list_start = time.time()  # 시작 시간 저장
        order_class_list = order_faker.create_order_dataset(user_class_list, product_class_list, 10000)
        print("10,000개 order_class_list time :", time.time() - order_class_list_start)  # 현재시각 - 시작시간 = 실행 시간

        print("order_class_list for문 실행")
        order_class_list_for_start = time.time()  # 시작 시간 저장
        for order_class in order_class_list:
            order = Order()
            order.created_at = order_class.createdAt
            order.amount = order_class.amount
            order.total_price = order_class.totalPrice
            order.product_id = order_class.product_id
            order.user_id = order_class.user_id
            session.add(order)
        print("order_class_list for문 time :", time.time() - order_class_list_for_start)

        print("session commit 실행")
        session_commit_start = time.time()
        session.commit()
        print("session commit time :", time.time() - session_commit_start)
        print(i + 1, "번 째 저장완료!")


    # print("#====== restock_notification table에 저장 ======#")
    # # Restock_Notification 100,000개 생성
    # restock_notification_faker = RestockNotificationFaker()
    # restock_notification_class_list = restock_notification_faker.create_restock_notification_dataset(user_class_list, product_class_list, 1000)
    # for restock_notification_class in restock_notification_class_list:
    #     restock_notification = RestockNotification()
    #     restock_notification.created_at = restock_notification_class.created_at
    #     restock_notification.alarm_flag = restock_notification_class.alarm_flag
    #     restock_notification.product_id = restock_notification_class.product_id
    #     restock_notification.user_id = restock_notification_class.user_id
    #     session.add(restock_notification)
    # session.commit()

    print("모든 테이블 저장 완료!")
    # session 종료
    session.close()