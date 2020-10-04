# coding=utf-8
import os
import json


def get_eval_item():
    files = os.listdir('eval_total_jd/')
    for ind, fi in enumerate(files):
        print ind, fi
        with open('eval_total_jd/%s' % fi, 'r') as s:
            # noinspection PyBroadException
            try:
                tmp = json.load(s)
            except:
                print 'error'
                continue
            sentences = tmp.values()[0]
            for sentence in sentences:
                if (u'默认' in sentence and u'好评' in sentence) or u'未评价' in sentence or u'填写' in sentence:
                    print sentence
                    continue
                with open('eval_negative/eval_jd_negative_20190102.txt', 'a') as f:
                    f.write(sentence.encode('utf-8').replace('\n', '。') + '\n')


if __name__ == '__main__':
    get_eval_item()
