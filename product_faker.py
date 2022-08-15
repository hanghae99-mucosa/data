from table.Product import Product
from faker import Faker
from faker.providers import DynamicProvider
import user_faker
import brand_faker
import category_faker

fake = Faker('ko_KR')

def create_product_dataset(brand_class_list, categroy_class_list, num):

    product_class_list = []

    product_brand_id_provider = DynamicProvider(
        provider_name="set_brand_id_in_product",
        elements=brand_class_list,
    )

    fake.add_provider(product_brand_id_provider)


    product_category_id_provider = DynamicProvider(
        provider_name="set_category_id_in_product",
        elements=categroy_class_list,
    )

    fake.add_provider(product_category_id_provider)

    for i in range(1, num + 1):
        brand_class = fake.set_brand_id_in_product()
        brand_id = brand_class.brand_id
        name = fake.name()
        thumbnail = "http://localhost:8080" + fake.file_path(category='image', extension='png')
        category_class = fake.set_category_id_in_product()
        category_id = category_class.category_id

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

        amount = fake.pyint(min_value=0, max_value=999)
        review_num = fake.pyint(min_value=0, max_value=50000)
        
        review_avg = round(fake.pyfloat(min_value=0, max_value=5), 1)
        if (review_avg < 1):
            review_avg = 0

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
        print(product)
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

    print(len(product_class_list))