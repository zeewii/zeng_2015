#coding=utf-8
#描述：本模块实现通过ssh登录远程主机后修改远程主机文件名
#作者：曾祥卫

from ssh import ssh_pexpect
from public import public
import scp



#输入：filename-文件名(也可以是文件的路径)，user-登录名,ip-登录ip,
    # password-登录密码,dir-远程主机的文件路径(也可以远程主机的文件名)
#输出：无
def modify_remote_file(user,ip,password,dir,filename,content):
    #登录远程主机并删除对应的文件
    ssh_pexpect.ssh_command(user,ip,password,'rm -rf %s%s'%(dir,filename))
    print '删除远程主机的文件%s%s成功'%(dir,filename)
    #在本地先新建或打开文件，并写入内容
    public.modify_file(filename,content)
    #通过scp传输给远程主机
    scp.scp(filename,ip,user,password,dir)
    print '修改远程主机文件%s%s成功'%(dir,filename)


'''if __name__ == "__main__":
    filename = '11'
    ip = '192.168.88.11'
    user = 'zeng'
    password = 'zeng'
    dir = '/home/zeng/ftp/'
    content = ['1\n','2\n','3\n']

    modify_remote_file(user,ip,password,dir,filename,content)'''

