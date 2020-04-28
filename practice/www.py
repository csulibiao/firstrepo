## convert www.zhidao.baidu.com to com/baidu/zhidao/www"
token = c95c7322ebcd644e7ba4b875dbd7bc3cbb369ef2
astr='www.zhidao.baidu.com'
print('/'.join(astr.split('.')[::-1]))