
import hashlib
import requests


token = "42892efb860b294a999a27448d59d598d6d03218"
baseURL = "https://lambda-treasure-hunt.herokuapp.com/api/bc"
def get_header():
    return {
        "Content-Type": "application/json",
        "Authorization": f"Token {token}"
    }
res = requests.get(f"{baseURL}/last_proof/", headers=get_header())
proof = 0
# Without calling res = res.json(), don't think you need to put the
# response in [" "] instead of dot notation
last_proof = res.get("proof")
diff = res.get("difficulty")
print(f"last proof: {last_proof}")
print(f"difficulty: {diff}")
guess = f'{last_proof}{proof}'.encode()
guess_hash = hashlib.sha256(guess).hexdigest()
hash_start = ""
for i in range(diff):
    hash_start += "0"
print(f"leading zeros to find: {hash_start}")
while guess_hash[:diff] != hash_start:
    proof += 2
    new_proof = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(new_proof).hexdigest()
    

res = requests.post(f"{baseURL}/mine/", headers=get_header(), json={"proof": proof}) 
print(f"good proof:  {proof}")
print(f"response: {res.json()}")
last_proof = proof
proof = 0