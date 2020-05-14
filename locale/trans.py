f = 'ru/LC_MESSAGES/django.po'

rr = open(f, mode='r', encoding='utf-8')
res = {}
for r in rr:
    tr = r.find('msgid')
    print(tr)
# dd = rr.readlines()
# dd = rr.read()
rr.close()

