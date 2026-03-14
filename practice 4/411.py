import json
def patch_json(source,patch):
    for key, value in patch.items():
        if value is None:
            source.pop(key,None)
        elif key in source and isinstance(source[key],dict) and isinstance(value,dict):
            patch_json(source[key],value)
        else:
            source[key]=value
    return source
s=json.loads(input())
p=json.loads(input())
print(json.dumps(patch_json(s,p), sort_keys=True, separators=(',',':')))