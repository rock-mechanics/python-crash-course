
from user import User

class Admin(User) : 
    def __init__(self, first , last,  **params): 
        # user provide a argument sequence.
        # **params match the sequence and pack them into params
        # to call the method __init__ in super class, we need to provided the sequences
        super().__init__(first, last, **params)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self) : 
        print('You have the following privileges : ')
        for p in self.privileges: 
            print(" - {}".format(p))
