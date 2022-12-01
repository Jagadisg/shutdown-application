import os
class ShutDown:
    def __init__(self):
        pass
    def restarttime(self,time):
        inp = time.get()
        hh,mm,ss = inp.split(':')
        sec =  int(hh)*3600+int(mm)*60+int(ss)
        os.system(f"shutdown /r /t {sec}")
    def restart(self):
        os.system("shutdown /r /t 1")
    def logout(self):
        os.system("shutdwon -l")
    def shutdown(self):
        os.system("shutdown /s /t 1")
st = ShutDown()
