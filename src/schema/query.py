#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Zella Zhong
Date: 2024-08-28 22:21:45
LastEditors: Zella Zhong
LastEditTime: 2024-08-29 17:32:22
FilePath: /cryptodata_apollographql/src/schema/query.py
Description: 
'''
import logging
import strawberry
from pydantic import typing
from typing import Annotated, Union
from typing import Optional, List, TypeVar, Generic
from strawberry.types import Info

from scalar import Domain
from scalar.error import PlatformNotSupport
from resolver import basename_domain_query

T = TypeVar("T")

@strawberry.input
class AbelFilter(Generic[T]):
    eq: Optional[T] = None
    gt: Optional[T] = None
    lt: Optional[T] = None


@strawberry.input
class WhereFilter:
    # bar: Optional[AbelFilter[int]] = None
    name: Optional[AbelFilter[str]] = None
    owner: Optional[AbelFilter[str]] = None


@strawberry.type
class Query:
    @strawberry.field
    async def domain(self, info: Info, platform: str, name: str) -> Domain:
        """ Get domain by name """
        logging.debug(f"Get domain by name {name}")
        if platform == "basenames":
            single_domain = await basename_domain_query(info, name)
            return single_domain
        else:
            return PlatformNotSupport(platform)

    @strawberry.field
    async def domains(self, info: Info, where: WhereFilter) -> str:
        
        return str(where)
