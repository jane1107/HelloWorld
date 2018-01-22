import requests
import random

my_numbers = random.sample(range(1,46), 6)

url = 'http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo='
res = requests.get(url).json()  # res responses의 준말
  
drw_numbers=[]
for i in range(1,7):
  drw_numbers.append(res['drwtNo'+str(i)])
bonus_number = res['bnusNo']

print("이번 주 로또 번호는 ", drw_numbers)
print("보너스 번호는 ", bonus_number)