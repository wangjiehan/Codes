import os
import json


files = os.listdir('eval_total_tm')

for f  in files:
    print(f)
    with open('eval_total_tm/%s' % f, 'r') as s:
        data = json.load(s)
        for d in data:
            with open('eval_negative/eval_tm_20181229.txt', 'a') as j:
                j.write(d['rateContent'].encode('utf-8') + '\n')
