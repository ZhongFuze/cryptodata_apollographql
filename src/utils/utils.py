#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Zella Zhong
Date: 2024-08-28 21:32:19
LastEditors: Zella Zhong
LastEditTime: 2024-08-29 00:37:22
FilePath: /cryptodata_apollographql/src/utils/utils.py
Description: 
'''
import logging
from sqlalchemy.inspection import inspect
import re

def convert_camel_case(name):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    name = pattern.sub('_', name).lower()
    return name

def get_only_selected_fields(db_baseclass_name, info):
    db_relations_fields = inspect(db_baseclass_name).relationships.keys()
    selected_fields = [convert_camel_case(field.name)  for field in info.selected_fields[0].selections if field.name not in db_relations_fields]
    selected_fields = [getattr(db_baseclass_name, f) for f in selected_fields]
    return selected_fields

def check_valid_data(model_data_object, model_class):
    data_dict = {}
    for column in model_class.__table__.columns:
        try:
            data_dict[column.name] = getattr(model_data_object,column.name)
        except:
            pass
    return data_dict