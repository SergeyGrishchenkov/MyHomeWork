class TVController:
     def __init__(self, cannels_list):
         self.cannels_list = cannels_list

    def first_channel(self): #  - turns on the first channel from the list.
    def last_channel(self): #  - turns on the last channel from the list.
    def turn_channel(self,N): #  - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
    def next_channel(self): # - turns on the next channel. If the current channel is the last one, turns on the first channel.
    def previous_channel(self): #  - turns on the previous channel. If the current channel is the first one, turns on the last channel.
    def current_channel(self): #  - returns the name of the current channel.
    def is_exist(name): # - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.