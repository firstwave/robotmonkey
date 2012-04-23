from sikuli import *
import seemonkey

print('listeners.sikuli inited')


class withVerboseKeywords:
    ROBOT_LISTENER_API_VERSION = 2

    def start_keyword(self, name, attrs):
        print(name)

class withSnapshots:
    ROBOT_LISTENER_API_VERSION = 2 
    
    def end_test(self, name, attrs):
        print("snapshot saved to results/snapshots/" + name + ".png")