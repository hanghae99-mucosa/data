class Category:
    """
    Category Class
    """
    
    def __init__(self, category_id, category, parent_category):
        self.__category_id = category_id
        self.__category = category
        self.__parent_category = parent_category

    @property
    def category_id(self):   
        return self.__category_id

    @property
    def category(self):   
        return self.__category

    @property
    def parent_category(self):
        return self.__parent_category

    def __str__(self):
        return 'Category(category_id={0}, category={1}, parent_category={2})'.format(self.__category_id, self.__category, self.__parent_category)

