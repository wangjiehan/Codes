files = ['service.txt', 'service_.txt']

for fil in files:
    with open('eval_class/%s' % fil, 'r') as s:
        data = s.readlines()
        print(len(data))
        data = set(data)
        print(len(data))
        for d in data:
            with open('eval_class/_%s' % fil, 'a') as t:
                t.write(d)
