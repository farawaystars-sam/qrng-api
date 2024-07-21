# testing the api endpoint /random_bit_string
import requests, json

cases = [(3, None), (10, 1), (100, 10)]
local_host = "http://127.0.0.1:5000"
end_point="/random_int"
responses = {}
count = 0
n_count = 0
for max, min in cases:
    params ={
        'max':max,
        'min': min
    }
    print(params)
    res = requests.get(local_host+end_point, params=params)
    res = json.loads(res.text)
    print(res)
    if min <= res['rand_int'] and max > res['rand_int']:
        responses[(max, min)] = "OK"
        count += 1
    else:
        responses[(max, min)] = "NOT OK"
        n_count += 1

print(responses)
print("Number of OK responses:", count)
print("Number of NOT OK responses:", n_count)
print(f"\n\n[OK]    Successfuly tested end-point {end_point} with service {count/(count+n_count)*100:.2f} %\n\n")