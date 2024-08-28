#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Zella Zhong
Date: 2024-08-28 21:15:34
LastEditors: Zella Zhong
LastEditTime: 2024-08-29 00:17:53
FilePath: /cryptodata_apollographql/src/model/__init__.py
Description: 
'''
from sqlalchemy.ext.declarative import declarative_base

# declarative_base() is a factory function that constructs a base class
# for declarative class definitions (which is assigned to the Base variable in model).
Base = declarative_base()

from .post import Post