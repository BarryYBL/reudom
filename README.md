# reudom

Automated testing framework based on requests and unittest interface.

> 基于 Unittest 和 Requests 的 接口自动化测试框架
#### 介绍
基于Unittest/Requests的接口自动化测试库
* 提供脚手架，快速生成接口自动化测试项目。
* 自动生成HTML测试报告。
* 支持用例参数化。
* 支持用例失败重跑
* 对原生Requests库API无损

#### 目录架构
```
myreudom/
├── test_case/
│   ├── test_sample.py
├── reports/
└── run.py
```

* `test_dir/`目录实现用例编写。
* `reports/` 目录存放生成的测试报告。
* `run.py` 文件运行测试用例。


#### 安装教程

```shell
> pip install reudom
```

If you want to keep up with the latest version, you can install with github repository url:

```shell
> pip install -U git+https://github.com/BarryYBL/reudom.git@master
```

#### 创建项目
```shell
>reudom --project myreudom
```
#### 运行项目：

```shell
> reudom -r run.py
Python 3.7.1

  ━━━━━━神兽出没━━━━━━━
  　　　┏┓　　　┏┓
  　　┏┛┻━━━┛┻┓
  　　┃　　　　　　　┃
  　　┃　　　━　　　┃
  　　┃　┳┛　┗┳　┃
  　　┃　　　　　　　┃
  　　┃　　　┻　　　┃
  　　┃　　　　　　　┃
  　　┗━┓　　　┏━┛
  　　　　┃　　　┃  神兽保佑
  　　　　┃　　　┃  代码无bug　　
  　　　　┃　　　┗━━━┓
  　　　　┃　　　　　　　┣┓
  　　　　┃　　　　　　　┏┛
  　　　　┗┓┓┏━┳┓┏┛
  　　　　　┃┫┫　┃┫┫
  　　　　　┗┻┛　┗┻┛
  ━━━━━━感觉萌萌哒━━━━━━━
-------------------------
                             @itest.info

generated html file: file:/Users/work/reports/2019_12_22_14_51_57_result.html
.1
```

#### 查看报告

你可以到 `myreudom\reports\` 目录查看测试报告。

![](./test_report.png)

### simple demo

请查看 `demo/test_sample.py` 文件

```python
import reudom


class test(reudom.TestCase):
    def setUp(self):
        self.url = 'https://v3.cw360.com.cn/v3/api/pc/signup'

    def test01(self):
        data = {'ver': '3.1.3.7', 'platform': 'web', 'mobile_phone': '13120539912', 'verify_code': 'longri', 'location': ''}
        rep = reudom.request('post', url=self.url, headers=headers(), data=data)
        result = rep.json()
        self.assertEqual(result['user']['name'], '用户13120539919')
        print('name不等于登录时的手机号')


if __name__ == '__main__':
    reudom.main("test_sample.py")

```

__说明：__

* 创建测试类必须继承 `reudom.TestCase`。
* 测试用例文件命名必须以 `test` 开头。
* reudom引入了`post`、`get`、`head`、`patch`、`put`、`delete`、`options`等方法。

### main() 方法

```python
import reudom

# ...

if __name__ == '__main__':

    seldom.main(
              path="./",
              title="接口自动化测试用例", 
              description="详细测试结果：", 
              debug=False,
              rerun=0,
              save_last_run=False,
    )
```

说明：

* path ： 指定测试目录或文件。
* title ： 指定测试报告标题。
* description ： 指定测试报告描述。
* debug ： debug模式，设置为True不生成测试HTML测试，默认为`False`。
* rerun : 设置失败重新运行次数，默认为 `0`。
* save_last_run : 设置只保存最后一次的结果，默认为`False`。


### Run the test

```python
import reudom

reudom.main(path="./")  # 当前目录下的所有测试文件
reudom.main(path="./test_dir/")  # 指定目录下的所有测试文件
reudom.main(path="./test_dir/test_sample.py")  # 指定目录下的测试文件
reudom.main(path="test_sample.py")  # 指定当前目录下的测试文件
```

说明：

* 如果指定的目录，测试文件必须以`test` 开头。
* 如果要运行子目录下的文件，必须在子目录下加 `__init__.py` 文件。


### 跳过用例

```python
import reudom


class YouTest(reudom.TestCase):

    @reudom.skip("跳过这条用例的执行")
    def test_case(self):
        """a simple test case """
        #...

```
感谢虫师！借鉴seldom项目得到思路和帮助。

* [seldom](https://github.com/SeldomQA/seldom)

### 作者联系方式：
QQ：316 586 6425
Mail：YBL2652612315@126.com
