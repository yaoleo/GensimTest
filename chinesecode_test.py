#-*-coding:utf-8-*-
import re
#
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



for line in open('2016G201000_result.txt'):
    #line = line.decode("utf-8").encode('unicode')
    #print line
    #print unicode(line, 'utf-8')# 输出正常汉字 说明编码是UTF8
    line = re.findall(ur"[\u4e00-\u9fa5]+", line.decode("utf-8"))
    print [text for text in line]

