#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Zella Zhong
Date: 2024-08-29 01:39:58
LastEditors: Zella Zhong
LastEditTime: 2024-08-29 21:03:11
FilePath: /cryptodata_apollographql/src/scalar/domain.py
Description: 
'''
import strawberry

from datetime import datetime
from pydantic import Field, typing
from strawberry.scalars import JSON


DEFAULT_GRACE_PERIOD = 90 * 24 * 3600 # days


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
    # grace_period_ends: typing.Optional[int] = None
    grace_period_ends: strawberry.Private[typing.Optional[int]] = None
    owner: typing.Optional[str] = None
    resolver: typing.Optional[str] = None
    resolved_address: typing.Optional[str] = None
    reverse_address: typing.Optional[str] = None
    is_primary: bool = False
    contenthash: typing.Optional[str] = None
    update_time: typing.Optional[int] = None
    resolved_records: typing.Optional[JSON] = None
    key_value: typing.Optional[JSON] = None

    @strawberry.field(name="gracePeriodEnds")
    def grace_period_ended(self) -> typing.Optional[int]:
        if self.expire_time is None:
            return None
        else:
            if self.grace_period_ends is None:
                return self.expire_time + DEFAULT_GRACE_PERIOD
            else:
                return self.grace_period_ends
