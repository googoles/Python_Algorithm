import hashlib

data = b'Hello World'
hash_object = hashlib.sha256()                      # 어떤 해쉬 알고리즘 쓸래?
hash_object.update(data)                            # 어떤 값을 해슁할 것인가?
hex_dig = hash_object.hexdigest()                   # 16진수로 해쉬값을 리턴해줌
print(hex_dig)
a = b'a'
print(type(a))