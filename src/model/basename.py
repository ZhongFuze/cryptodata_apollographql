#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Zella Zhong
Date: 2024-08-29 02:00:40
LastEditors: Zella Zhong
LastEditTime: 2024-08-29 02:42:43
FilePath: /cryptodata_apollographql/src/model/basename.py
Description: 
'''
import time
import logging
from datetime import datetime
from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, DateTime, BigInteger, JSON
from pydantic.color import Optional
from pydantic import typing
from sqlalchemy.types import TypeDecorator
from urllib.parse import unquote

from . import Base


class DatetimeToTimestamp(TypeDecorator):
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

class Basename(Base):
    """Post"""
    __tablename__ = "basenames"
    id: int = Column(Integer, primary_key=True, index=True)
    namenode: str = Column(String, unique=True, index=True)
    name: str = Column(String, index=True, nullable=True)
    label: str = Column(String, nullable=True)
    token_id: str = Column(String, nullable=True)
    parent_node: str = Column(String, nullable=True)

    owner: str = Column(String, index=True, nullable=True)
    resolver: str = Column(String, nullable=True)
    resolved_address: str = Column(String, index=True, nullable=True)
    reverse_address: str = Column(String, index=True, nullable=True)
    is_primary: bool = Column(Boolean)

    registration_time: int = Column(DatetimeToTimestamp, nullable=True)
    expire_time: int = Column(DatetimeToTimestamp, nullable=True)
    update_time: int = Column(DatetimeToTimestamp, nullable=True)

    resolved_records: dict = Column(JSON, nullable=True)
    contenthash: str = Column(String, nullable=True)
    key_value: dict = Column(JSON, nullable=True)

    def as_dict(self):
        return {
            "namenode": self.namenode,
            "name": self.name,
            "label": self.label,
            "token_id": self.token_id,
            "parent_node": self.parent_node,
            "registration_time": self.registration_time,
            "expire_time": self.expire_time,
            "owner": self.owner,
            "resolver": self.resolver,
            "resolved_address": self.resolved_address,
            "reverse_address": self.reverse_address,
            "is_primary": self.is_primary,
            "update_time": self.update_time,
            "resolved_records": self.resolved_records,
            "key_value": self.key_value,
        }
