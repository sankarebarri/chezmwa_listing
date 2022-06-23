import uuid

def generate_house_code():
    code = str(uuid.uuid4()).replace('-','').upper()[:12]
    return code
