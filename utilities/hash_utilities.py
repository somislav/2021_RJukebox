import hashlib
from enum import Enum


class Algorithm(Enum):
    SHA1 = 'sha1',
    SHA256 = 'sha256',
    MD5 = 'md5'


def generate_hash(password: str, algorithm: Algorithm = Algorithm.SHA256) -> str:
    try:
        if algorithm == Algorithm.SHA256:
            hasher = hashlib.sha256()
        elif algorithm == Algorithm.SHA1:
            hasher = hashlib.sha1()
        elif algorithm == Algorithm.MD5:
            hasher = hashlib.md5()
        else:
            raise Exception("Incompatible algorithm used. Choose from: sha256 | sha1 | md5")

        hasher.update(password.encode('utf-8'))
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error happpened while hashing: {e}")
        return ""