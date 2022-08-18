class Restock_Notification:
    """
    Restock_Notification Class
    """
    
    def __init__(self, restock_id, user_id, product_id, alarm_flag):
        self.__restock_id = restock_id
        self.__user_id = user_id
        self.__product_id = product_id
        self.__alarm_flag = alarm_flag

    @property
    def restock_id(self):   
        return self.__restock_id

    @property
    def user_id(self):   
        return self.__user_id

    @property
    def product_id(self):   
        return self.__product_id

    @property
    def alarm_flag(self):   
        return self.__alarm_flag


    def __str__(self):
        return 'Restock_Notification(restock_id={0}, user_id={1}, product_id={2}, alarm_flag={3})'.format(self.__restock_id, self.__user_id, self.__product_id, self.__alarm_flag)
