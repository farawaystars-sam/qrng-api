# testing the api endpoint /random_bit_string
import requests, json

cases = [1, 10, 20, 100, 10000]
local_host = "http://127.0.0.1:5000"
end_point="/random_bit_string"
responses = {}
count = 0
n_count = 0
for n in cases:
    params ={
        'n':n
    }
    res = requests.get(local_host+end_point, params=params)
    if n == len(json.loads(res.text)['bit_string']):
        responses[n] = "OK"
        count += 1
    else:
        responses[n] = "NOT OK"
        n_count += 1

print(responses)
print("Number of OK responses:", count)
print("Number of NOT OK responses:", n_count)
print(f"\n\n[OK]    Successfuly tested end-point {end_point} with service {count/(count+n_count)*100:.2f} %\n\n")