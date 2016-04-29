from  main  import MB,B
import re
import os
import shutil
kk = MB()
# kk.multi(5, 6)
# MB.multi(5,6)
kk.multi(2,9)
kk.sub(9,2)
kk.sub(2,9)
s = re.search('click','click input')


print '[-------s333333333------------]'
s2 = re.search('[iI]nput|[cC]lick','Input input Click click')
print s2
if s2:
    print s2.string

print '[-------s333333333------------]'
s3 = re.search(r'[iI]nput|[cC]lick','Input Click ')
print s3
if s3:
    print s3.string
# if __name__ == '__main__':

current_dir = os.path.abspath('.')
shutil.rmtree('test')
os.mkdir('test')
my_dir =  os.path.join(current_dir,'test')
print '[>>>]my dir',my_dir
shutil.rmtree('test')

for item in os.listdir(current_dir):
    if os.path.splitext(item)[1] == '.png' or os.path.splitext(item)[1] =='.gif':
        print item

        # print os.path.abspath(item)
        # print current_dir+'\\'+item
        # print current_dir+'\\'+current_test+'\\'+item
        # shutil.move(current_output_dir+'\\'+item,current_output_dir+'\\'+name+'\\'+item)
print '----------------------------------------------'
