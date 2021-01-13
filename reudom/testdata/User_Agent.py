"""
User-Agent 浏览器用户代理
* 支持 PC 端用户代理：Chrome、Safari、IE、Firefox
* 支持 移动端 用户代理：Chrome_phone、Safari_phone、IE_phone、Firefox_phone
"""


def Chrome():
    """PC--Chrome"""
    Agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) " \
            "AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    return Agent


def Safari():
    """PC--Safari"""
    Agent = "User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) " \
            "AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    return Agent


def IE():
    """PC--IE"""
    Agent = "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
    return Agent


def Firefox():
    """PC--Firefox"""
    Agent = "User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
    return Agent


def Chrome_phone():
    """phone--Chrome"""
    Agent = "User-Agent: Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) " \
            "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
    return Agent


def Safari_phone():
    """phone--Safari"""
    Agent = "User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) " \
            "AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"
    return Agent


def IE_phone():
    """phone--IE"""
    Agent = "User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; " \
            "IEMobile/9.0; HTC; Titan)"
    return Agent


def Firefox_phone():
    """phone--Firefox"""
    Agent = "User-Agent: Mozilla/5.0 (Androdi; Linux armv7l; rv:5.0) Gecko/ Firefox/5.0 fennec/5.0"
    return Agent


chromePC = Chrome()
safariPC = Safari()
iePC = IE()
firefoxPc = Firefox()

chromePhone = Chrome_phone()
safariPhone = Safari_phone()
iePhone = IE_phone()
firefoxPhone = Firefox_phone()

if __name__ == '__main__':
    print(Chrome())
