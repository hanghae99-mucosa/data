#-*- coding: utf-8 -*-
from sqlalchemy import BigInteger, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import BIT, DATETIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Category(Base):
    __tablename__ = 'category'

    category_id = Column(BigInteger, primary_key=True)
    category = Column(String(150), nullable=False)
    parent_category = Column(BigInteger)


class User(Base):
    __tablename__ = 'user'

    user_id = Column(BigInteger, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    role = Column(Integer)


class Brand(Base):
    __tablename__ = 'brand'

    brand_id = Column(BigInteger, primary_key=True)
    name = Column(String(255), unique=True)
    user_id = Column(ForeignKey('user.user_id'), nullable=False, index=True)

    user = relationship('User')


class Product(Base):
    __tablename__ = 'product'

    product_id = Column(BigInteger, primary_key=True)
    amount = Column(Integer, nullable=False)
    name = Column(String(150), nullable=False)
    price = Column(Integer, nullable=False)
    review_avg = Column(Float, nullable=False)
    review_num = Column(Integer, nullable=False)
    thumbnail = Column(String(255))
    brand_id = Column(ForeignKey('brand.brand_id'), nullable=False, index=True)
    category_id = Column(ForeignKey('category.category_id'), nullable=False, index=True)

    brand = relationship('Brand')
    category = relationship('Category')


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(BigInteger, primary_key=True)
    created_at = Column(DATETIME(fsp=6))
    amount = Column(Integer, nullable=False)
    total_price = Column(Integer, nullable=False)
    product_id = Column(ForeignKey('product.product_id'), nullable=False, index=True)
    user_id = Column(ForeignKey('user.user_id'), nullable=False, index=True)

    product = relationship('Product')
    user = relationship('User')


class RestockNotification(Base):
    __tablename__ = 'restock_notification'

    restock_id = Column(BigInteger, primary_key=True)
    alarm_flag = Column(BIT(1))
    product_id = Column(ForeignKey('product.product_id'), nullable=False, index=True)
    user_id = Column(ForeignKey('user.user_id'), nullable=False, index=True)

    product = relationship('Product')
    user = relationship('User')
