from transitions import Machine
class Door(object):
    states = ['closed', 'opened', 'locked']
    pin = '0000'

    def __init__(self):
        self.machine = Machine(model=self, states=Door.states, initial='locked')
        self.machine.add_transition('open_storage', 'closed', 'opened')
        self.machine.add_transition('close_storage', 'opened', 'closed')
        self.machine.add_transition('block_storage', 'closed', 'locked')
        self.machine.add_transition('unblock_storage', 'locked', 'closed')





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
