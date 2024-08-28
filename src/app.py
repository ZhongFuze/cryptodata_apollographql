#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Zella Zhong
Date: 2024-08-28 19:02:56
LastEditors: Zella Zhong
LastEditTime: 2024-08-29 00:26:00
FilePath: /cryptodata_apollographql/src/app.py
Description: 
'''
import os
import uvicorn
import logging
import strawberry

from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

import setting
import setting.filelogger as logger
from schema import Query, Mutation

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    config=StrawberryConfig(
        auto_camel_case=True
    )
)


def create_app():
    app = FastAPI()
    graphql_app = GraphQLRouter(schema)
    app.include_router(graphql_app, prefix="/graphql")
    @app.get("/")
    async def hello_world():
        logging.info("Hello World")
        return {"message": "Hello World"}
    return app


def set_log_config():
    uvicorn_log_config = uvicorn.config.LOGGING_CONFIG
    format = "[%(asctime)s - %(levelname)s %(process)s %(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    uvicorn_log_config["formatters"]["access"]["fmt"] = format
    uvicorn_log_config["formatters"]["default"]["fmt"] = format
    return uvicorn_log_config

application = create_app()

if __name__ == "__main__":
    config = setting.load_settings(env=os.getenv("ENVIRONMENT"))
    if not os.path.exists(config["server"]["log_path"]):
        os.makedirs(config["server"]["log_path"])

    worker_number = config["server"]["process_count"]
    logger.InitLogger(config)
    logging.info(f"Starting server {worker_number} process ...")
    # uvicorn.run("app:application", host="127.0.0.1", port=5000, workers=worker_number, log_level=logging.INFO)
    uvicorn.run("app:application", host="127.0.0.1", port=5000, reload=True, log_level=logging.INFO)
