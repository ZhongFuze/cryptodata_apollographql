#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Zella Zhong
Date: 2024-08-28 21:21:20
LastEditors: Zella Zhong
LastEditTime: 2024-08-29 01:28:35
FilePath: /cryptodata_apollographql/src/model/post.py
Description: 
'''
import time
import logging
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, BigInteger
from pydantic.color import Optional
from sqlalchemy.orm import synonym
from sqlalchemy.dialects.postgresql import BIGINT
from sqlalchemy.types import TypeDecorator

from . import Base

class UnixToDatetime(TypeDecorator):
    # convert unix timestamp to datetime object
    impl = BigInteger

    # convert datetime object to unix timestamp when inserting data to database
    def process_bind_param(self, value, dialect=None):
        if value is not None:
            return int(value.timestamp())
        else:
            return None

    def process_result_value(self, value, dialect=None):
        return datetime.fromtimestamp(value)

class Timestamp(TypeDecorator):
    # convert unix timestamp to datetime object
    impl = DateTime

    # convert datetime object to unix timestamp when inserting data to database
    def process_bind_param(self, value, dialect=None):
        return datetime.fromtimestamp(value)

    def process_result_value(self, value, dialect=None):
        if value is not None:
            return int(value.timestamp())
        else:
            return None


class Post(Base):
    """Post"""
    __tablename__ = "test_table"
    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String, nullable=True)
    description: str = Column(String, nullable=True)
    # created_at: DateTime = Column(DateTime, nullable=False)
    created_at: int = Column(Timestamp, nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at,
        }