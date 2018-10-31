#!/bin/env python
#-*- encoding: UTF-8 -*-
from datetime import datetime
from pprint import pprint

def ts_to_utctime(ts):
    dt = datetime.fromtimestamp(ts)
    utc_time = dt.strftime('%Y-%m-%d %H:%M:%S')
    return utc_time
