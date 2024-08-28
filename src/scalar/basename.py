#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Zella Zhong
Date: 2024-08-29 01:39:58
LastEditors: Zella Zhong
LastEditTime: 2024-08-29 02:36:59
FilePath: /cryptodata_apollographql/src/scalar/basename.py
Description: 
'''
import strawberry

from datetime import datetime
from pydantic import Field, typing
from strawberry.scalars import JSON


@strawberry.type(
    name="basename",
    description="Basenames are built on the decentralized, open source ENS protocol, aligned \
        with Base's dedication to decentralized and open source technologies.")
class Basename:
    namenode: str
    name: typing.Optional[str] = ""
    label: typing.Optional[str] = None
    token_id: typing.Optional[str] = None
    parent_node: typing.Optional[str] = ""
    registration_time: typing.Optional[int] = None
    expire_time: typing.Optional[int] = None
    owner: typing.Optional[str] = None
    resolver: typing.Optional[str] = None
    resolved_address: typing.Optional[str] = None
    reverse_address: typing.Optional[str] = None
    is_primary: bool = False
    contenthash: typing.Optional[str] = None
    update_time: typing.Optional[datetime] = Field(default_factory=datetime.now)
    resolved_records: typing.Optional[JSON] = None
    key_value: typing.Optional[JSON] = None


@strawberry.type
class BasenameNotFound:
    message: str = "Couldn't find basename by given name"

@strawberry.type
class BasenameInvalid:
    message: str = "given name is not a valid basename"
