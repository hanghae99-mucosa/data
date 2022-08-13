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


    product_categroy_id_provider = DynamicProvider(
        provider_name="set_categroy_id_in_product",
        elements=categroy_class_list,
    )

    fake.add_provider(product_categroy_id_provider)

    for i in range(1, num + 1):
        brand_class = fake.set_brand_id_in_product()
        brand_id = brand_class.brand_id
        name = fake.name()
        thumbnail = "http://localhost:8080" + fake.file_path(category='image', extension='png')
        category_class = fake.set_categroy_id_in_product()
        category_id = category_class.category_id
        price = fake.pyint(min_value=1000, max_value=10000000, step=100)
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

    for product in product_class_list:
        print(product)

    print(len(product_class_list))