
from transitions import Machine
import time

class Door(object):
    states = ['closed', 'opened', 'locked']
    pin = '0000'

    def __init__(self):
        self.machine = Machine(model=self, states=Door.states, initial='locked')
        self.machine.add_transition('open_storage', 'closed', 'opened')
        self.machine.add_transition('close_storage', 'opened', 'closed', before='start_timer')
        self.machine.add_transition('block_storage', 'closed', 'locked')
        self.machine.add_transition('unblock_storage', 'locked', 'closed', before='start_timer')

    def start_timer(self):
        print('В доработке')
        #self.close_time = time.time()

    def is_locked(self):
        print('В доработке')
        #return (time.time() - self.close_time) > 45

    #def close_storage(self):
        #if self.is_locked():
        #    self.block_storage()
       # else:
            #self.machine.set_state('closed')




#door = Door()
#print(door.state)  # выведет "closed"
#door.open_storage()
#print(door.state)  # выведет "opened"
#door.close_storage()
#print(door.state)  # выведет "closed"
#door.block_storage()
#print(door.state)  # выведет "locked"
#door.unblock_storage()
#print(door.state)  # выведет "closed"
