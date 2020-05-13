import hashlib
from devtools import debug


def sign_avro(avro:dict) -> str:
    fields = avro['fields']
    signed = {item['name']:item['type'] for item in fields}
    lines = []
    for k in sorted(signed.keys()):
        v = signed[k]
        if isinstance(v,list):
            value = ":".join(sorted(v))
        else:
            value = v
        lines.append("{key}__{value}".format(key=k, value=value))
    raw = "&".join(lines)
    return hashlib.md5(raw.encode('utf-8')).hexdigest()