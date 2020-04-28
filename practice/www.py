## convert www.zhidao.baidu.com to com/baidu/zhidao/www"
token = 'f4c228c2874889992f85cf012008befb3df197c0'
astr='www.zhidao.baidu.com'
print('/'.join(astr.split('.')[::-1]))