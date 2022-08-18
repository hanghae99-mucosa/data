class Order:
    """
    Order Class
    """
    
    def __init__(self, order_id, user_id, product_id, amount, totalPrice, createdAt):
        self.__order_id = order_id
        self.__user_id = user_id
        self.__product_id = product_id
        self.__amount = amount
        self.__totalPrice = totalPrice
        self.__createdAt = createdAt

    @property
    def order_id(self):   
        return self.__order_id

    @property
    def user_id(self):   
        return self.__user_id

    @property
    def product_id(self):   
        return self.__product_id

    @property
    def amount(self):   
        return self.__amount

    @property
    def totalPrice(self):   
        return self.__totalPrice

    @property
    def createdAt(self):   
        return self.__createdAt

    def __str__(self):
        return 'Order(order_id={0}, user_id={1}, product_id={2}, amount={3}, totalPrice={4}, createdAt={5})'.format(self.__order_id, self.__user_id, self.__product_id, self.__amount, self.__totalPrice, self.__createdAt)
