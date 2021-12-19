#!/usr/bin/env python3

# Module to encode and decode JWT
import jwt
# Module to encode and decode base64
import base64
# Module to create and validate HMAC
import hmac
# Modile of hashing libraries
import hashlib

# The HMAC secret key
mykey = bytes('secretkey', 'utf-8')
# Bytes containing a dot
bytesdot = bytes('.', 'utf-8')
# The JWT header
myhead = '{"typ":"jwt","alg":"HS256"}'
print("\nJWT Header: ", myhead, "\n")
# Encode header as bytes
myhead = myhead.encode()
# The JWT payload
mypay = '{"username": "adrien","role": "user" }'
print("JWT Payload: ", mypay, "\n")
# Encoded payload as bytes
mypay = mypay.encode()

# Concatenate base64 URL encoded header, a dot, and base64 URL encoded payload
unsignedjwt = base64.urlsafe_b64encode(myhead) + bytesdot + base64.urlsafe_b64encode(mypay)
# Strip off any trailing = signs
unsignedjwt = unsignedjwt.rstrip(b'=')
# Show the unsigned JWT
print("Unsigned JWT: ", unsignedjwt.decode('utf-8'), "\n")

# Create the JWT signature which is base64 URL encoded HMAC-256 signed bytes
mysig = base64.urlsafe_b64encode(hmac.new(mykey, unsignedjwt, digestmod=hashlib.sha256).digest())
# Strip off any trailing = signs
mysig = mysig.rstrip(b'=')
# Show the JWT signature
print("JWT HS256 signature: ", mysig.decode('utf-8'), "\n")

# Create the JWT by concatenating the header, payload, and signature separated by a dot
signedjwt = unsignedjwt + bytesdot + mysig
# Show the final JWT
print("Full signed JWT: ", signedjwt.decode('utf-8'), "\n")
# Decode it correctly using pyJWT
print("Decoded JWT: ", jwt.decode(signedjwt, mykey), "\n")

