#!/usr/bin/env python3
import jwt

payload = {'user_id': 'adrien'}
jwt_token = jwt.encode(payload, None, 'none')
print(jwt_token)
jwt_decode = jwt.decode(jwt_token)
print(jwt_decode)
