import requests

aes_url = 'http://tool.chacuo.net/cryptaes'

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'

}

ECB = 'ecb'
PKC = 'pkcs5'
BLOCK = '128'
PWD = '123'
IV = '123456'
O = '0'
S = 'gb2312'
T = '0'


ARG = 'm='+ECB+'_pad='+PKC+'_block='+BLOCK+'_p='+PWD+'_i='+IV+'_o='+'O'+'_s='+'gb2312'+'_t='+'0'
print(ARG)
data = {
    'data': '土豆',
    'type': 'aes',
    'arg': ARG
}

result = requests.post(url=aes_url, headers=header, data=data)
print(result.text)
