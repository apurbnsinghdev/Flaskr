import jsonrpclib

s = jsonrpclib.Server('https://suman@amberit.com.bd:2XSH67MMD8praRu4@www.safedns.com/api/json')

t = s.systemInfo()

print t


