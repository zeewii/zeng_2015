#coding=utf-8
#描述：本模块实现通过scp拷贝文件到另一个主机上
#作者：曾祥卫

import pexpect
#描述：本函数实现通过scp拷贝文件到另一个主机上
#输入：filename-文件名(也可以是文件的路径)，user-登录名,ip-登录ip,
    # password-登录密码,dir-远程主机的文件路径(也可以远程主机的文件名)
#输出：无
def scp(filename,ip,user,password,dir):
    try:
        # 为scp命令生成一个spawn类的子程序对象
        child = pexpect.spawn('scp %s %s@%s:%s'%(filename,user,ip,dir))
        #列出期望出现的字符串，'password',EOF，超时'
        i = child.expect(["(?i)password",pexpect.EOF,pexpect.TIMEOUT])

        #如果没有匹配到了密码字符
        if i != 0:
            print u"scp要求输入密码时出现EOF或超时"
        #如果匹配到了密码字符
        child.sendline(password)

        #列出输入密码后期望出现的字符串，'password',EOF，超时'
        i = child.expect(["(?i)password",pexpect.EOF,pexpect.TIMEOUT])
        #匹配到pexpect.EOF，
        if i == 0:
            print u'密码输入错误！'
        elif i == 1:
            print u'恭喜,传输成功！'
        else:
            print u'传输文件超时！'

    except pexpect.ExceptionPexpect, e:
        print u"scp连接失败",str(e)



'''if __name__ == '__main__':
    filename = '/home/zeng/22'
    ip = '192.168.88.11'
    user = 'zeng'
    password = 'zeng'
    dir = '/home/zeng/ftp/'
    scp(filename,ip,user,password,dir)'''










__author__ = 'zeng'
