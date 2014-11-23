__author__ = 'kangxi'

import urllib,urllib2,re
char = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n''o','p','q','r','s','t','u','v','w','x','y','z')
t1 = []
t2 = []
url = 'http://www.zgsj.com/domain_reg/domainsub.asp'
filename = 'domain.txt'
f = file(filename, 'w')

for i1 in char:
    l1 = i1
    t1.append(l1)
    for i2 in char:
        l2 = l1+i2
        t1.append(l2)
        #for i3 in char:
            #l3 = l2+i3
           # t1.append(l3)
           # for i4 in char:
           #     l4 = l3+i4
           #     t1.append(l4)
           #     for i5 in char:
            #        l5 = l4+i5
            #        t1.append(l5)

for name in t1:
    value = {'name': '%s.com' % name}
    data = urllib.urlencode(value)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    page = response.read()
    item = name+'/.com'
    print(re.findall(item, page))
    if re.findall(str(value), page):
        f.write(str(value)+'ok')
        f.write(' ')
    else:
        f.write(str(value)+'no')
        f.write(' ')
        pass
print 'over'
f.close()