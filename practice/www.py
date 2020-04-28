## convert www.zhidao.baidu.com to com/baidu/zhidao/www"
token = '677a67d1cc97ad2a2f2a70ecd1a61a6a84bb86e0'
astr='www.zhidao.baidu.com'
print('/'.join(astr.split('.')[::-1]))