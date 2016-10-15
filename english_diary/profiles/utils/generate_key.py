import random

from hashids import Hashids


def generate_user_activation_key(user_id):

        hashids = Hashids(
            salt=str(random.random()),
            min_length=30,
        )
        encoded_hashids = hashids.encode(user_id)
        return encoded_hashids
