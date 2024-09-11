#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name='Favoured', last_name='Mwange'):
        super().__init__(first_name,last_name)
        self.knowledge = []
    
    def learn(self,new_information):
        # pass
        if isinstance(new_information,str) and new_information:
            self.knowledge.append(new_information)