import hashlib
from devtools import debug


def sign_avro(avro:dict) -> str:
    fields = avro['fields']
    signed = {item['name']:item['type'] for item in fields}
    lines = []
    for k in sorted(signed.keys()):
        lines.append("{key}_{value}".format(key=k, value=signed[k]))
    raw = "&".join(lines)
    debug(raw)
    return hashlib.md5(raw.encode('utf-8')).hexdigest()