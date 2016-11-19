from engine import engine
from Config_paser import start_parser
from __Threading import ThreadManager

if __name__ == '__main__' :
    start_parser()
    engine.sendToSchedule()
    thread = ThreadManager()
    thread.add_func_get()
    thread.start_thread()
    thread.waitForallThreadcompelete()
    engine.GetfromSchedule()