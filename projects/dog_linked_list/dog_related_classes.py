#!/usr/bin/python2.7

class AryaTheDog(object):
    ''' This class creates a description about a dog '''
    def __init__(self, description_value):
      self.description_value = description_value
      self.next = None



class AllAboutArya(object):
    ''' This class creates a linked list of the descriptions of the dog, including
    ways to append new descriptions, get position in list, and delete descriptions. '''
    def __init__(self, start=None):
      self.start = start
      

    def append(self, new_description):
        current_description = self.start
        if self.start:
            while current_description.next:
                current_description = current_description.next
            current_description.next = new_description
            #print('\n\tcurrent_description.next: ' + str(new_description))
        else:
          self.start = new_description
          #print('\n\tself.start: ' + str(new_description))

    def get_dog_description_position(self,position_of_dog_description):
        description_counter = 1
        current_description = self.start
        if position_of_dog_description < 1:
            return None
        while current_description and description_counter <= position_of_dog_description:
            if description_counter == position_of_dog_description:
                return current_description
            current_description = current_description.next
            description_counter += 1
        return None
    
    def insert_new_description(self,new_description,position_of_dog_description):
        description_counter = 1
        current_description = self.start
        if position_of_dog_description > 1:
            while description_counter < position_of_dog_description:
                    if description_counter == position_of_dog_description - 1:
                        new_description.next = current_description.next
                        current_description.next = new_description
                    current_description = current_description.next
                    description_counter += 1
        elif position_of_dog_description == 1:
            new_description.next = self.start
            self.start = new_description
        
    def delete_old_description(self,position_to_delete):      
        current_position = 1
        current = self.start
        previous = None
        #If we are supposed to delete the first one
        #print('\n\n\tChecking position: ' + str(current_position))
        #print('\tCurrent description: ' + current.description_value)
        if current_position == position_to_delete:
            #print('\t\tRemoving description: ' + current.description_value)
            self.start = current.next
        else:
            #Loop over (position 2 - position_to_delete)
            #Start at position 2
            previous = current
            current = current.next
            current_position += 1 #this is now 2, the first time
            while current_position <= position_to_delete and current.next:
                #print('\n\tChecking position: ' + str(current_position))
                #print('\tPrevious description: ' + previous.description_value)
                #print('\tCurrent description: ' + current.description_value)
                #print('\tNext description: ' + current.next.description_value)

                #If we hit the position we are supposed to delete
                if current_position == position_to_delete:
                        #print('\t\tRemoving description: ' + current.description_value)
                        previous.next = current.next
                        return
                #If we are not in the position to delete
                else:
                    previous = current
                    current = current.next
                    current_position += 1
            #print('\n\tThere are no more items in the linked list')

                
                
