#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import redis
redis = redis.Redis(host = '127.0.0.1')
redis.set('name','kevin')
print(redis.get('name'))
