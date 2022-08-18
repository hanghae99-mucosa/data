class User:
    """
    User Class
    """
    
    def __init__(self, user_id, email, password, role):
        self.__user_id = user_id
        self.__email = email
        self.__password = password
        self.__role = role

    @property
    def user_id(self):   
        return self.__user_id

    @property
    def email(self):   
        return self.__email

    @property
    def password(self):   
        return self.__password


    @property
    def role(self):   
        return self.__role

    def __str__(self):
        return 'User(user_id={0}, email={1}, password={2}, role={3})'.format(self.__user_id, self.__email, self.__password, self.__role)
