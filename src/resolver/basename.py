import logging
from datetime import datetime
from sqlalchemy import select, update
from sqlalchemy.orm import load_only
from urllib.parse import unquote

from session import get_session
from utils import get_only_selected_fields, check_valid_data, compute_namehash_nowrapped
from model import Basename
from scalar import BasenameNotFound, BasenameInvalid


async def basename_domain(info, name):
    if not name.endswith("base.eth"):
        return BasenameInvalid
    query_namenode = compute_namehash_nowrapped(name)
    logging.info("Query basenames={}, namenode={}".format(name, query_namenode))
    selected_fields = get_only_selected_fields(Basename, info)
    async with get_session() as s:
        sql = select(Basename).options(load_only(*selected_fields)) \
        .filter(Basename.namenode == query_namenode)
        db_result = (await s.execute(sql)).scalars().unique().one()

    if db_result is None:
        return BasenameNotFound()

    basename_dict = check_valid_data(db_result, Basename)
    if "key_value" in basename_dict:
        if basename_dict["key_value"] is not None:
            for key, text in basename_dict["key_value"].items():
                basename_dict["key_value"][key] = unquote(text, 'utf-8')

    return Basename(**basename_dict)