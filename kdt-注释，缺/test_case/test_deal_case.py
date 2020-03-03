
class Test_deal:
    def __init__(self):
        pass

    def read_case(self,filename):
        with open(filename,'r+',encoding='utf8') as f:
            li_top=[]
            li_step=[]
            li=[]
            lines=f.readlines()

            for line in lines:
                line=line.strip()
                # print(line,type(line))      s2:input id,username,admin <class 'str'>
                # 下面就是用例标题和步骤的分离
                if line[0:2]=='tc':     # 做到这一步，就要定义出几个空列表，用来装标题和步骤
                    line = line.split(':')[0]
                    li_top.append(line)

                elif line[0:1]=='s':
                    step=[]                   # 每一个步骤就是一个列表
                    line=line.split(':',1)[1]     # 步骤里，用  :  分割，分割一次，因为后面可能还会有  ：
                    # print(line,type(line))
                    step.append(line)            # 把步骤封装到列表中
                    li_step.append(step)

                elif line[0:3]=='end':    # 用 end 做一个用例的结束，
                    li.append(li_top)      # 定义了一个空列表用来装全部的头和步骤
                    li.append(li_step)
                    li_top=[]              # 一定要清空用来装步骤和头的列表，不然列表会越来越多
                    li_step=[]
            # print(li)
            return li

if __name__ == '__main__':
    a=Test_deal()
    a.read_case('web_case')
