import requests


try:
    response = requests.get("http://pudim.com.br/")
    if response.status_code == 200:
        print('site pudim no ar')
except Exception as e:
    print(e)
    print('site pudim fora do ar')


