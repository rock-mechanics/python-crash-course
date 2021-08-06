class User() : 
    def __init__(self, first, last, **params): 
        self.first_name = first
        self.last_name = last
        self.info = params
    def describe_user(self): 
        print('{} {}'.format(self.first_name.title(), self.last_name.title()))
        for key, value in self.info.items() : 
            print('\t{} : {}'.format(key, value))
    def greet_user(self): 
        print('hi, {}'.format(self.first_name.title()))

            
