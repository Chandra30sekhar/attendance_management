from hashlib import md5

def encrypt(s):
    s = s.encode('utf-8')
    s = md5(s).hexdigest()
    return s
