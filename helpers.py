import uuid

def generate_random_string(length=8):
    return uuid.uuid4().hex[:length]
