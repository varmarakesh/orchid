import glob
import json
from orchid import orchid

profiles = glob.glob('json/*.json')

for profile in profiles:
    r = orchid(inputJson=json.loads(open(profile).read()))
    print profile
    print r.url, r.path, r.host, r.submission_date, r.creation_method
