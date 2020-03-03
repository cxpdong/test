from test_case.test_deal_case import Test_deal
from web.web_key import key

class run:
    def __init__(self,filename):
        self.li = Test_deal().read_case(filename)
        self.num = len(self.li)
        self.key = key()

    def do_web_case(self):
        # print(self.li)
        for tit in self.li[0:self.num:2]:
            if tit[0][0:2]=='tc':
                for step in self.li[1:self.num:2][0]:
                    # print(step)
                    active = step[0].split(' ',1)[0]
                    note = step[0].split(' ',1)[1].split(',')

                    if active=='open':
                        print(note[1])
                        getattr(self.key,'open')(note[1])

                    if active == 'input':
                        getattr(self.key, 'input')(note[0],note[1],note[2])

                    if active == 'click':
                        getattr(self.key, 'click')(note[0],note[1])

if __name__ == '__main__':
    r = run('../test_case/web_case')
    r.do_web_case()
