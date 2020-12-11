
import time
import requests
from faker import Faker

def sleep(n_secs):
    time.sleep(n_secs)


def get_mobile():
    faker = Faker("zh_CN")
    mobile = faker.phone_number()
    return mobile

def get_token():
    url = 'https://passportdev.doushen.com/userve/user/login'
    header = {'Content-Type':'application/x-www-form-urlencoded'}
    data = {'user_account':'18600712596',
            'verify_data':'123456hj',
            'login_type':'1'}
    res = requests.post(url,data,headers=header)
    # token = res.json().get('data').get('token')
    # print(res.json())
    token = res.json()['data']['token']
    # token = json['data']['token']

    return token

if __name__ == '__main__':
    print(get_mobile())
    print(get_token())