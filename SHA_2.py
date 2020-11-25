from hashlib import sha256

msg = 'I love python'
sha = sha256()
sha.update(msg.encode('utf-8'))
ret = sha.hexdigest()

print('SHA-2 SHA-256', ret)
