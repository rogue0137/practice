#!/usr/bin/python2.7

import dog_related_classes

#creating descriptions of arya
description_one = dog_related_classes.AryaTheDog('wags her tail')
description_two = dog_related_classes.AryaTheDog('loves peanut butter')
description_three = dog_related_classes.AryaTheDog('is super tiny and adorable')
description_four = dog_related_classes.AryaTheDog('furiously awesome')

#instantiating the class of AllAboutArya and appending descriptions
descriptions_of_arya = dog_related_classes.AllAboutArya(description_one)
descriptions_of_arya.append(description_two)
descriptions_of_arya.append(description_three)
descriptions_of_arya.append(description_four)

print('Initial description_values:')
print('description of arya start description_value: ' + descriptions_of_arya.start.description_value)
print('description of arya next description_value: ' + descriptions_of_arya.start.next.description_value)
print('description of arya next next description_value: ' + descriptions_of_arya.start.next.next.description_value)
print('descriptions of arya, description in first position: ' + str(descriptions_of_arya.get_dog_description_position(1).description_value))
print('descriptions of arya, description in second position: ' + str(descriptions_of_arya.get_dog_description_position(2).description_value))
print('descriptions of arya, description in third position: ' + str(descriptions_of_arya.get_dog_description_position(3).description_value))
print('descriptions of arya, description in fourth position: ' + str(descriptions_of_arya.get_dog_description_position(4).description_value))

#insert new descriptions into AllAboutArya
description_five = dog_related_classes.AryaTheDog('has a brother named Poe')
description_six = dog_related_classes.AryaTheDog('lives in DTLA')

descriptions_of_arya.insert_new_description(description_five,1)
descriptions_of_arya.insert_new_description(description_six,3)

print('\n')
print('Description_values after insertion:')
print('description of arya start description_value: ' + descriptions_of_arya.start.description_value)
print('description of arya next description_value: ' + descriptions_of_arya.start.next.description_value)
print('description of arya next next description_value: ' + descriptions_of_arya.start.next.next.description_value)
print('descriptions of arya, description in first position: ' + str(descriptions_of_arya.get_dog_description_position(1).description_value))
print('descriptions of arya, description in second position: ' + str(descriptions_of_arya.get_dog_description_position(2).description_value))
print('descriptions of arya, description in third position: ' + str(descriptions_of_arya.get_dog_description_position(3).description_value))
print('descriptions of arya, description in fourth position: ' + str(descriptions_of_arya.get_dog_description_position(4).description_value))
print('descriptions of arya, description in fifth position: ' + str(descriptions_of_arya.get_dog_description_position(5).description_value))
print('descriptions of arya, description in sixth position: ' + str(descriptions_of_arya.get_dog_description_position(6).description_value))

#delete descriptions from AllAboutArya
descriptions_of_arya.delete_old_description(1)
descriptions_of_arya.delete_old_description(4)

print('\n')
print('Description values after deletion:')
print('description of arya start description_value: ' + descriptions_of_arya.start.description_value)
#print('description of arya next description_value: ' + descriptions_of_arya.start.next.description_value)
#print('description of arya next next description_value: ' + descriptions_of_arya.start.next.next.description_value)
print('descriptions of arya, description in first position: ' + str(descriptions_of_arya.get_dog_description_position(1).description_value))
print('descriptions of arya, description in second position: ' + str(descriptions_of_arya.get_dog_description_position(2).description_value))
print('descriptions of arya, description in third position: ' + str(descriptions_of_arya.get_dog_description_position(3).description_value))
print('descriptions of arya, description in fourth position: ' + str(descriptions_of_arya.get_dog_description_position(4).description_value))
