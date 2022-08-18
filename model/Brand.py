class Brand:
    """
    Brand Class
    """
    
    def __init__(self, brand_id, name, user_id):
        self.__brand_id = brand_id
        self.__name = name
        self.__user_id = user_id

    @property
    def brand_id(self):   
        return self.__brand_id

    @property
    def name(self):   
        return self.__name

    @property
    def user_id(self):   
        return self.__user_id

    def __str__(self):
        return 'Brand(brand_id={0}, name={1}, user_id={2})'.format(self.__brand_id, self.__name, self.__user_id)
