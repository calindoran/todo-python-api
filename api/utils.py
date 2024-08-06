from datetime import datetime, timedelta

import jwt
from django.conf import settings


def generate_access_token(user):
    payload = {
        'user_id': user.user_id,
        'exp': datetime.now() + timedelta(days=1, minutes=0),
        'iat': datetime.now(),
    }

    access_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return access_token
