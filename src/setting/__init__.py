#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Zella Zhong
Date: 2024-08-28 19:38:25
LastEditors: Zella Zhong
LastEditTime: 2024-08-28 19:40:18
FilePath: /cryptodata_apollographql/src/setting/__init__.py
Description: 
'''
import sys
import logging
import os
import toml


Settings = {
    "env": "development",
    "datapath": "./data",
}

PG_DSN = {
    "cryptodata": "",
}

def load_settings(env="test"):
    """
    @description: load configurations from file
    """
    global Settings
    global PG_DSN

    config_file = "/app/config/production.toml"
    if env == "testing":
        config_file = "/app/config/testing.toml"
    elif env == "development":
        config_file = "./config/development.toml"
    elif env == "production":
        config_file = "/app/config/production.toml"
    else:
        raise ValueError("Unknown environment")

    config = toml.load(config_file)
    Settings["env"] = env
    Settings["datapath"] = os.path.join(config["server"]["work_path"], "data")
    PG_DSN = load_dsn(config_file)
    return config


def load_dsn(config_file):
    """
    @description: load pg dsn
    @params: config_file
    @return dsn_settings
    """
    try:
        config = toml.load(config_file)
        pg_dsn_settings = {
            "cryptodata": config["pg_dsn"]["cryptodata"],
        }
        return pg_dsn_settings
    except Exception as ex:
        logging.exception(ex)