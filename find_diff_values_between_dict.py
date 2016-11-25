# coding: UTF-8
before=[{u'UserName':u'@b53413e822cf67a219ab7181b074ccf5', u'RemarkPYQuanPin':u'', u'DisplayName': u'', u'KeyWord': u'iss', u'PYInitial': u'', u'Uin': 12266535, u'MemberStatus': 0, u'PYQuanPin': u'', u'RemarkPYInitial': u'', u'NickName': u'\u4e00\u4e8c\u4e09', u'AttrStatus': 2181050407L}, {u'UserName': u'@4babcdd9789c909048a51a069eb37b635f4f79bc5dfc2b5ae6e7325e16848e2b', u'RemarkPYQuanPin': u'', u'DisplayName': u'\u6696\u6696\u7684o', u'KeyWord': u'', u'PYInitial': u'', u'Uin': 1589615073, u'MemberStatus': 0, u'PYQuanPin': u'', u'RemarkPYInitial': u'', u'NickName': u'\u6696\u6696\u7684', u'AttrStatus': 4133}, {u'UserName': u'@1f6ddf50c372ba088a9b8f61670a8cfa5873ede35810a60b4076486eac6c20e2', u'RemarkPYQuanPin': u'', u'DisplayName': u'', u'KeyWord': u'', u'PYInitial': u'', u'Uin': 2720082935L, u'MemberStatus': 0, u'PYQuanPin': u'', u'RemarkPYInitial': u'', u'NickName': u'\u5929\u5929\u60e0\uff5e\u6dd8\u5b9d\u7f51\u5185\u90e8\u6298\u6263', u'AttrStatus': 102469}, {u'UserName': u'@f0142b2f34421927607e46c7c5894fcdb46bdaa173b354ef0d93c7950a3016ac', u'RemarkPYQuanPin': u'', u'DisplayName': u'', u'KeyWord': u'', u'PYInitial': u'', u'Uin': 3048262847L, u'MemberStatus': 0, u'PYQuanPin': u'', u'RemarkPYInitial': u'', u'NickName': u'\u6298\u6263\u53d1\u5e03\u5458Summer', u'AttrStatus': 102469}, {u'UserName': u'@15b51f37927a241f2e0f537c8b446280bdfacd73a8adeacf6db2db096c837a0b', u'RemarkPYQuanPin': u'', u'DisplayName': u'', u'KeyWord': u'', u'PYInitial': u'', u'Uin': 3379331828L, u'MemberStatus': 0, u'PYQuanPin': u'', u'RemarkPYInitial': u'', u'NickName': u'\u7075\u7075\u516b', u'AttrStatus': 4133}]
now=[{u'UserName': u'@9233910c70034bc94ccd683157f5760f600f2bd25ac70c4bb66fd501caca8a8e', u'RemarkPYQuanPin': u'', u'DisplayName': u'\u6696\u6696\u7684o', u'KeyWord': u'', u'PYInitial': u'', u'Uin': 1589615073, u'RemarkPYInitial': u'', u'PYQuanPin': u'', u'MemberStatus': 0, u'NickName': u'\u6696\u6696\u7684', u'AttrStatus': 16781349}, {u'UserName': u'@d5131e8ac7df644c522c9293914b70fe5ebee374f0d42c58157b516a567a7dae', u'RemarkPYQuanPin': u'', u'DisplayName': u'', u'KeyWord': u'', u'PYInitial': u'', u'Uin': 2720082935L, u'RemarkPYInitial': u'', u'PYQuanPin': u'', u'MemberStatus': 0, u'NickName': u'\u5929\u5929\u60e0\uff5e\u6dd8\u5b9d\u7f51\u5185\u90e8\u6298\u6263', u'AttrStatus': 2147586117L}, {u'UserName': u'@bd7fc47cfb0c9a3f85505c3794d2945ae46edf28c4e68613993f1aaac480b92a', u'RemarkPYQuanPin': u'', u'DisplayName': u'', u'KeyWord': u'', u'PYInitial': u'', u'Uin': 3048262847L, u'RemarkPYInitial': u'', u'PYQuanPin': u'', u'MemberStatus': 0, u'NickName': u'\u6298\u6263\u53d1\u5e03\u5458Summer', u'AttrStatus': 102469}]


re=dict()


for d in before:             # add values to each set() from dicts in list_before
    if isinstance(d, dict):
        for k in d.keys():
            if k not in re.keys():
                re[k]=set()
            re[k].add(d[k])


for d in now:                 # remove values that in list_now's dicts
    if isinstance(d, dict):
        for k in d.keys():
            if d[k] in  re[k]:
                #print d[k]
                re[k].remove(d[k])
                #if len(re[k])>1:
                #    re[k].remove(d[k])

for item in re.keys():
    if re[item]==set([]):  # delete keys whose value is set(u'')  
        print item
        del re[item]
        
print re 
