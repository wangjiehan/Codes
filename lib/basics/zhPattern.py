import re
zhPattern = re.compile(u'[\u4e00-\u9fa5]+')

contents = "f324gaxz"
match = zhPattern.search(contents)

if match:
    print('有中文：%s' % (match.group(0),))
else:
    print('没有包含中文')
