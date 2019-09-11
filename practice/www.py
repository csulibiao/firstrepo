## convert www.zhidao.baidu.com to com/baidu/zhidao/www"

astr='www.zhidao.baidu.com'
print('/'.join(astr.split('.')[::-1]))