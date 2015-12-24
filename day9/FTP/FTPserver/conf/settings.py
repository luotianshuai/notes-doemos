#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIND_HOST = '127.0.0.1'
BIND_PORT = 9999

USER_ACCOUNT = {
    'shuaige':{'password':'21232f297a57a5a743894a0e4a801fc3',
            'quotation': 1000000, #1GB
            'expire': '2016-01-22'
            },
    'tianshuai':{'password':'21232f297a57a5a743894a0e4a801fc3',
        'quotation': 2000000, #2GB
        'expire': '2016-01-22'
        },
}


USER_HOME = USER_HOME = '%s/var/' %BASE_DIR

