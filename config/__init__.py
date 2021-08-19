# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸 (Blueking) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

import os

__author__ = "蓝鲸智云"
__copyright__ = "Copyright © 2012-2019 Tencent BlueKing. All Rights Reserved."
__all__ = ["celery_app", "ENVIRONMENT", "RUN_VER", "BK_URL", "BASE_DIR"]

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from blueapps.core.celery import celery_app

# app 基本信息


def get_env_or_raise(key):
    """Get an environment variable, if it does not exist, raise an exception"""
    value = os.environ.get(key)
    if not value:
        raise RuntimeError(
            ('Environment variable "{}" not found, you must set this variable to run this application.').format(key)
        )
    return value


# V3判断环境的环境变量为BKPAAS_ENVIRONMENT
if "BKPAAS_ENVIRONMENT" in os.environ:
    ENVIRONMENT = os.getenv("BKPAAS_ENVIRONMENT", "dev")
# V2判断环境的环境变量为BK_ENV
else:
    PAAS_V2_ENVIRONMENT = os.environ.get("BK_ENV", "development")
    ENVIRONMENT = {"development": "dev", "testing": "stag", "production": "prod"}.get(PAAS_V2_ENVIRONMENT)

# SaaS运行版本，如非必要请勿修改
# 暂时避开开发框架的问题，新版PaaS该值设置为default
# 在开发框架中根据该值导入config，config仅提供open可选
RUN_VER = os.environ.get("ENGINE_REGION", "open")

APP_ID = APP_CODE = os.environ.get("APP_ID", "bk_gsekit")
APP_TOKEN = SECRET_KEY = os.environ.get("APP_TOKEN", "28b7b410-c7b7-4537-9a65-8ce55738170e")

# 蓝鲸平台URL
BK_URL = os.getenv("BKPAAS_URL", None)  # noqa

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
