import hashlib
from devtools import debug
from enum import Enum

class MetaStatus(Enum):
    SUCCESS = 0
    NO_PRIMARY_KEY = 1


def check_avro(avro:dict) -> MetaStatus:
    has_primary_key = False
    fields = avro['fields']
    for field in fields:
        primary_key = field.get("primary_key")
        if primary_key:
            has_primary_key = True
            break
    if has_primary_key is False:
        return MetaStatus.NO_PRIMARY_KEY 
    return MetaStatus.SUCCESS

def sign_avro(avro:dict) -> str:
    fields = avro['fields']
    signed = {item['name']:item['type'] for item in fields}
    primary = {item['name']:item.get('primary_key',False) for item in fields}
    lines = []
    for k in sorted(signed.keys()):
        v = signed[k]
        if isinstance(v,list):
            value = ":".join(sorted(v))
        else:
            value = v
        line = "{key}__{value}".format(key=k, value=value)
        primary_key = primary[k]
        if primary_key:
            line = line + "primary=true"
        lines.append(line)
    raw = "&".join(lines)
    return hashlib.md5(raw.encode('utf-8')).hexdigest()