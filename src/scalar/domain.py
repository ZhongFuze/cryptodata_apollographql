#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Zella Zhong
Date: 2024-08-29 01:39:58
LastEditors: Zella Zhong
LastEditTime: 2024-08-29 17:13:39
FilePath: /cryptodata_apollographql/src/scalar/domain.py
Description: 
'''
import strawberry

from datetime import datetime
from pydantic import Field, typing
from strawberry.scalars import JSON


@strawberry.type
class Domain:
    id: strawberry.Private[object]
    namenode: typing.Optional[str] = ""
    name: typing.Optional[str] = ""
    label: typing.Optional[str] = None
    erc721_token_id: typing.Optional[str] = None
    erc1155_token_id: typing.Optional[str] = None
    parent_node: typing.Optional[str] = ""
    registration_time: typing.Optional[int] = None
    expire_time: typing.Optional[int] = None
    is_wrapped: bool = False
    fuses: typing.Optional[int] = 0
    grace_period_ends: typing.Optional[int] = None
    owner: typing.Optional[str] = None
    resolver: typing.Optional[str] = None
    resolved_address: typing.Optional[str] = None
    reverse_address: typing.Optional[str] = None
    is_primary: bool = False
    contenthash: typing.Optional[str] = None
    update_time: typing.Optional[int] = None
    resolved_records: typing.Optional[JSON] = None
    key_value: typing.Optional[JSON] = None

