#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Zella Zhong
Date: 2024-08-28 22:21:45
LastEditors: Zella Zhong
LastEditTime: 2024-08-29 02:46:21
FilePath: /cryptodata_apollographql/src/schema/query.py
Description: 
'''
import logging
import strawberry
from pydantic import typing
from strawberry.types import Info

from scalar import Post, Basename
from resolver import list_posts, get_post
from resolver import basename_domain


@strawberry.type
class Query:
    @strawberry.field
    async def list_posts(self, info:Info) -> typing.List[Post]:
        """ Get all posts """
        logging.debug("Get all posts")
        post_list = await list_posts(info)
        return post_list
    
    @strawberry.field
    async def get_post(self, info:Info, post_id: int) -> Post:
        """ Get post by id """
        logging.debug(f"Get post by post_id {post_id}")
        single_post = await get_post(info, post_id)
        return single_post

    @strawberry.field
    async def domain(self, info:Info, name: str) -> Basename:
        """ Get domain by name """
        logging.debug(f"Get domain by name {name}")
        single_domain = await basename_domain(info, name)
        return single_domain