CHANNELS = ["BBC", "Discovery", "TV1000"]
class TVController:
    def __init__(self, channels_list):
        self.channels_list = channels_list
        self.cur_channel = self.channels_list[0]

    def first_channel(self):  # - turns on the first channel from the list.
        self.cur_channel = self.channels_list[0]

    def last_channel(self):  # - turns on the last channel from the list.
        self.cur_channel = self.channels_list[len(self.channels_list) - 1]

    def turn_channel(self, chanel_number: int):  # - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
        if chanel_number in range(1, len(self.channels_list) + 1):
            self.cur_channel = self.channels_list[chanel_number - 1]
        else:
            print("Be more attentive!!! Such channel is not exist!")

    def next_channel(self):  # - turns on the next channel. If the current channel is the last one, turns on the first channel.
        current_index = self.channels_list.index(self.cur_channel)
        self.cur_channel = self.channels_list[current_index + 1 if current_index < (len(self.channels_list) - 1) else 0]

    def previous_channel(self):  # - turns on the previous channel. If the current channel is the first one, turns on the last channel.
        current_index = self.channels_list.index(self.cur_channel)
        self.cur_channel = self.channels_list[len(self.channels_list) - 1 if current_index == 0 else current_index - 1]

    def current_channel(self):  # - returns the name of the current channel.
        return self.cur_channel

    def is_exist(self, name_number):  # - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
        if isinstance(name_number, int):
            if name_number in range(1, len(self.channels_list) + 1):
                return 'Yes'
        else:
            if self.channels_list.count(name_number) > 0:
                return 'Yes'
        return 'No'


controller = TVController(CHANNELS)
#---
controller.first_channel()
print(controller.cur_channel)
#---
controller.last_channel()
print(controller.cur_channel)
#---
controller.turn_channel(1)
print(controller.cur_channel)
#---
controller.next_channel()
print(controller.cur_channel)
#---
controller.previous_channel()
print(controller.cur_channel)
#---
controller.current_channel()
print(controller.cur_channel)
#---
print(controller.is_exist(4))
print(controller.is_exist("BBC"))
#---
