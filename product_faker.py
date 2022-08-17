from table.Product import Product
from faker import Faker
from faker.providers import DynamicProvider
import user_faker
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
def create_product_dataset(brand_class_list, categroy_class_list, num):

    product_class_list = []

    product_brand_id_provider = DynamicProvider(
        provider_name="set_brand_id_in_product",
        elements=brand_class_list,
    )

    fake.add_provider(product_brand_id_provider)

    # 상위 카테고리를 뺀 나머지 카테고리 리스트
    category_list_without_parent_category = categroy_class_list[9:]
    product_category_id_provider = DynamicProvider(
        provider_name="set_category_id_in_product",
        elements=category_list_without_parent_category,
    )

    fake.add_provider(product_category_id_provider)

    for i in range(1, num + 1):
        brand_class = fake.set_brand_id_in_product()
        brand_id = brand_class.brand_id
        name = fake.name()
        category_class = fake.set_category_id_in_product()
        category_id = category_class.category_id

        # 카테고리 별 thumbnail 생성
        thumbnail_dict = {
            '상의': "/images/상의.png",
            '바지': "/images/바지.png",
            '아우터': "/images/아우터.png",
            '원피스': "/images/원피스.png",
            '스커트': "/images/스커트.png",
            '스니커즈': "/images/스니커즈.png",
            '신발': "/images/신발.png",
            '가방': "/images/가방.png"
        }
        parent_category = category_class.parent_cateogory
        thumbnail = thumbnail_dict[categroy_class_list[parent_category-1].category]

        # 약 70% 20% 5% 3% 2% 비율로 max_value 지정
        if i <= num * 0.6:
            price = fake.pyint(min_value=1000, max_value=100000, step=100)
        if num * 0.6 < i <= num * (0.6 + 0.3) + 1:
            price = fake.pyint(min_value=100000, max_value=500000, step=1000)
        if num * (0.6 + 0.3) + 1 < i <= num * (0.6 + 0.3 + 0.05):
            price = fake.pyint(min_value=500000, max_value=1000000, step=1000)
        if num * (0.6 + 0.3 + 0.05) < i <= num * (0.6 + 0.3 + 0.05 + 0.03):
            price = fake.pyint(min_value=1000000, max_value=5000000, step=1000)
        if num * (0.6 + 0.3 + 0.05 + 0.03) < i <= num * (0.6 + 0.3 + 0.05 + 0.03 + 0.02):
            price = fake.pyint(min_value=5000000, max_value=10000000, step=1000)

        # 1000개 생성시 10개 정도는 amount가 0 => 100번 째 마다 0 지정
        amount = 0
        if i % 100 != 0:
            amount = fake.pyint(min_value=1, max_value=999)

        review_avg = round(fake.pyfloat(min_value=0, max_value=5), 1)
        if review_avg < 1:
            review_avg = 0

        review_num = 0
        if review_avg != 0:
            review_num = fake.pyint(min_value=0, max_value=50000)

        product = Product(i, brand_id, name, thumbnail, category_id, price, amount, review_num, review_avg)
        product_class_list.append(product)

    return product_class_list


if __name__ == "__main__":
    
    user_class_list = user_faker.create_user_dataset(50)

    brand_class_list = brand_faker.create_brand_dataset(user_class_list, 100)

    categroy_class_list = category_faker.create_catogory_dataset()

    product_class_list = create_product_dataset(brand_class_list, categroy_class_list, 1000)

    range_1000_to_100000_cnt = 0
    range_100000_to_500000_cnt = 0
    range_500000_to_1000000_cnt = 0
    range_1000000_to_5000000_cnt = 0
    range_5000000_to_10000000_cnt = 0
    for product in product_class_list:
        price = product.price
        if 1000 <= price <= 100000:
            range_1000_to_100000_cnt += 1
        if 100000 < price <= 500000:
            range_100000_to_500000_cnt += 1
        if 500000 < price <= 1000000:
            range_500000_to_1000000_cnt += 1
        if 1000000 < price <= 5000000:
            range_1000000_to_5000000_cnt += 1
        if 5000000 < price <= 10000000:
            range_5000000_to_10000000_cnt += 1

    print("range_1000_to_100000_cnt : ", range_1000_to_100000_cnt)
    print("range_100000_to_500000_cnt : ", range_100000_to_500000_cnt)
    print("range_500000_to_1000000_cnt : ", range_500000_to_1000000_cnt)
    print("range_1000000_to_5000000_cnt : ", range_1000000_to_5000000_cnt)
    print("range_5000000_to_10000000_cnt : ", range_5000000_to_10000000_cnt)

    amount_0_cnt = 0
    for product in product_class_list:
        if product.amount == 0:
            amount_0_cnt += 1

    print("amount_0_cnt : ", amount_0_cnt)

    print(len(product_class_list))