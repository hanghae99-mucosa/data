from faker import Faker
from customFaker import category_faker
from customFaker.product_name_provider import ProductProvider
from faker.providers import DynamicProvider


fake = Faker('ko_KR')
fake.add_provider(ProductProvider)

categroy_class_list = category_faker.create_catogory_dataset()

# 상위 카테고리를 뺀 나머지 카테고리 리스트
category_list_without_parent_category = categroy_class_list[9:]
product_category_id_provider = DynamicProvider(
    provider_name="set_category_id_in_product",
    elements=category_list_without_parent_category,
)

fake.add_provider(product_category_id_provider)

product_name_list = []

for _ in range(100000):
    category_class = fake.set_category_id_in_product()
    parent_category = category_class.parent_cateogory
    category = categroy_class_list[parent_category - 1].category
    product_name = fake.product_name(category)
    product_name_list.append(product_name)

product_name_list_set = list(set(product_name_list))
print("상품명 개수 : ", len(product_name_list))
print("중복 제거 후 상품 개수 : ", len(product_name_list_set))