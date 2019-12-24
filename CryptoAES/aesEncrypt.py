from Crypto.Cipher import AES
import base64

class aesCrypt:
    def __init__(self, key, model, iv, encode_='GBK'):  #
        self.encode_ = encode_
        self.model = {'ECB': AES.MODE_ECB, 'CBC': AES.MODE_CBC, 'CFB': AES.MODE_CFB,
                      'OFB': AES.MODE_OFB, 'CTR': AES.MODE_CTR, 'OPENPGP': AES.MODE_OPENPGP}[model]
        self.key = self.add_16(key)

        if model == 'ECB':  # 这个里创建一个aes对象
            self.aes = AES.new(self.key, self.model)
        elif model == 'CBC':
            self.aes = AES.new(self.key, self.model, iv, segment_size=128)
        elif model == 'CFB':
            self.aes = AES.new(self.key, self.model)
        elif model == 'OFB':
            self.aes = AES.new(self.key, self.model)
        elif model == 'CTR':
            self.aes = AES.new(self.key, self.model)
        elif model == 'OPENPGP':
            self.aes = AES.new(self.key, self.model)

    # 这里的密钥长度必须是16、24或32
    def add_16(self, par):
        par = par.encode(self.encode_)
        while len(par) % 16 != 0:
            par += b'\x00'
        return par

    def aesEncrypt(self, text):  # text传入的是明文
        text = self.add_16(text)
        self.encrypt_text = self.aes.encrypt(text)
        print(base64.b64encode(self.encrypt_text).decode().strip())
        try:
            return base64.b64encode(self.encrypt_text).decode().strip()
        except Exception as error:
            return error