from model.Order import Order
from faker import Faker
from faker.providers import DynamicProvider
from customFaker.user_faker import UserFaker
from customFaker.brand_faker import BrandFaker
from customFaker.category_faker import CategoryFaker
from customFaker.product_faker import ProductFaker
from sqlalchemy import create_engine
from model.models import Product
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv
import pymysql
import time
import os

pymysql.install_as_MySQLdb()
load_dotenv()

host = os.environ.get("HOST")
port = os.environ.get("PORT")
username = os.environ.get("DB_USERNAME")
database = os.environ.get("DATABASE")
password = os.environ.get("PASSWORD")

DATABASE_PATH = 'mysql://{0}:{1}@{2}:{3}/{4}'.format(username, password, host, port, database)

fake = Faker('ko_KR')

def logging_time(original_fn):
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = original_fn(*args, **kwargs)
        end_time = time.time()
        print("WorkingTime[{}]: {} sec".format(original_fn.__name__, end_time-start_time))
        return result
    return wrapper_fn

class OrderFaker():
    @logging_time
    def create_order_dataset(self, user_class_list, product_class_list, num):
        engine = create_engine(DATABASE_PATH, pool_size=20, echo=False, future=True, encoding="utf-8", pool_recycle=3600)
        Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
        session = Session()

        product_query = session.query(Product).order_by(Product.product_id)

        order_class_list = []

        # order_user_id_provider = DynamicProvider(
        #     provider_name="set_user_in_order",
        #     elements=user_class_list,
        # )
        #
        # fake.add_provider(order_user_id_provider)

        # order_product_id_provider = DynamicProvider(
        #     provider_name="set_product_in_order",
        #     elements=product_class_list,
        # )
        #
        # fake.add_provider(order_product_id_provider)

        for i in range(1, num + 1):
            try:
                # user_class = fake.set_user_in_order()
                # user_id = user_class.user_id
                user_id = fake.pyint(min_value=1, max_value=371942)
                # product_class = fake.set_product_in_order()
                # product_id = product_class.product_id
                product_id = fake.pyint(min_value=1, max_value=1124563)
                amount = fake.pyint(min_value=1, max_value=10)
                product_query = session.query(Product).order_by(Product.product_id)
                product_class = product_query.get(product_id)
                product_price = product_class.price
                total_price = amount * product_price
                created_at = fake.date_time_between(start_date="-2y").isoformat("T", "auto")

                order = Order(i, user_id, product_id, amount, total_price, created_at)
                order_class_list.append(order)
                # session 종료
                session.close()
            except:
                # session 종료
                session.close()
                continue

        return order_class_list


if __name__ == "__main__":
    user_faker = UserFaker()
    user_class_list = user_faker.create_user_dataset(50)

    brand_faker = BrandFaker()
    brand_class_list = brand_faker.create_brand_dataset(user_class_list, 100)

    category_faker = CategoryFaker()
    category_class_list = category_faker.create_catogory_dataset()

    product_faker = ProductFaker()
    product_class_list = product_faker.create_product_dataset(brand_class_list, category_class_list, 1000)

    order_faker = OrderFaker()
    order_class_list = order_faker.create_order_dataset(user_class_list, product_class_list, 100)

    for order in order_class_list:
        print(order)

    print(len(order_class_list))
