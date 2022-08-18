class Product:
    """
    Product Class
    """
    
    def __init__(self, product_id, brand_id, name, thumbnail, category_id, price, amount, review_num, review_avg):
        self.__product_id = product_id
        self.__brand_id = brand_id
        self.__name = name
        self.__thumbnail = thumbnail
        self.__category_id = category_id
        self.__price = price
        self.__amount = amount
        self.__review_num = review_num
        self.__review_avg = review_avg

    @property
    def product_id(self):   
        return self.__product_id

    @property
    def brand_id(self):   
        return self.__brand_id

    @property
    def name(self):   
        return self.__name
    
    @property
    def thumbnail(self):   
        return self.__thumbnail

    @property
    def category_id(self):   
        return self.__category_id

    @property
    def price(self):   
        return self.__price

    @property
    def amount(self):   
        return self.__amount

    @property
    def review_num(self):   
        return self.__review_num

    @property
    def review_avg(self):   
        return self.__review_avg

    def __str__(self):
        return 'Product(product_id={0}, brand_id={1}, name={2}, thumbnail={3}, category_id={4}, price={5}, amount={6}, review_num={7}, review_avg={8})'.format(self.__product_id, self.__brand_id, self.__name, self.__thumbnail, self.__category_id, self.__price, self.__amount, self.__review_num, self.__review_avg)
