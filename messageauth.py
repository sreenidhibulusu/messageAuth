# https://coderzcolumn.com/tutorials/python/hashlib-compute-secure-hashes-message-digests-in-python
import hashlib


def MAC(message):
    keys = dict.fromkeys(range(1, 6))
    keys[1] = message
    shake_128_1 = hashlib.shake_128(message.encode())

    message_digest1 = shake_128_1.digest(15)
    keys[2] = message_digest1

    hex_message_digest1 = shake_128_1.hexdigest(15)
    keys[3] = hex_message_digest1

    shake_128_2 = hashlib.new("shake_128")
    shake_128_2.update(bytes(message, encoding="utf-8"))

    message_digest2 = shake_128_2.digest(15)
    keys[4] = message_digest2

    hex_message_digest2 = shake_128_2.hexdigest(15)
    keys[5] = hex_message_digest2

    return keys