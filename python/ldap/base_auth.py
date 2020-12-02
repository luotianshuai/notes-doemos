#! /usr/bin/python
# -*- coding:utf-8 -*-


from ldap3 import Server, Connection, SAFE_SYNC
server = Server('192.168.1.111', port=389, use_ssl=False)
conn = Connection(server, user='cn=shuai ge,ou=user,dc=tianshuai,dc=com',
                  password='123456s', client_strategy=SAFE_SYNC)

conn.bind()
if conn.result["description"] == "success":
    print(conn.result)
    # {'result': 0, 'description': 'success', 'dn': '', 'message': '', 'referrals': None, 'saslCreds': None, 'type': 'bindResponse'}
else:
    print(conn.result)
    print("验证失败")
    # {'result': 49, 'description': 'invalidCredentials', 'dn': '', 'message': '', 'referrals': None, 'saslCreds': None, 'type': 'bindResponse'}
