---
#HOW TO RUN: LINKED LISTS


These scripts an examples of creating linked lists in python. With these classes, several descriptions of the dog Arya are instantiated. The linked list **descriptions_of_arya** is then instantiated. Previously instantiated descriptions are added to **descriptions_of_arya** using a . Two further description are added using the method **insert_new description**. Later, the method **delete_old_description** is used to delete the description at position 1. After all descriptions have been reordered, the description at position 4 is also removed. There are print outs of results along the way.

##Run this code

Use Python 2.7

Clone this folder using 
```sh
$ git clone https://github.com/rogue0137/practice.git
```

cd into the appropriate folder
```sh
$ cd linked_lists
```

Then type
```sh
$ python dog_creation.py
```
 
See the following results printed
```sh

Initial description_values:
description of arya start description_value: wags her tail
description of arya next description_value: loves peanut butter
description of arya next next description_value: is super tiny and adorable
descriptions of arya, description in first position: wags her tail
descriptions of arya, description in second position: loves peanut butter
descriptions of arya, description in third position: is super tiny and adorable
descriptions of arya, description in fourth position: furiously awesome


Description_values after insertion:
description of arya start description_value: has a brother named Poe
description of arya next description_value: wags her tail
description of arya next next description_value: lives in DTLA
descriptions of arya, description in first position: has a brother named Poe
descriptions of arya, description in second position: wags her tail
descriptions of arya, description in third position: lives in DTLA
descriptions of arya, description in fourth position: loves peanut butter
descriptions of arya, description in fifth position: is super tiny and adorable
descriptions of arya, description in sixth position: furiously awesome


Description values after deletion:
description of arya start description_value: wags her tail
descriptions of arya, description in first position: wags her tail
descriptions of arya, description in second position: lives in DTLA
descriptions of arya, description in third position: loves peanut butter
descriptions of arya, description in fourth position: furiously awesome
``` 

##And in case you were interested...

<img src="http://i.imgur.com/VqRzvF2.jpg" width="244" height="326" alt="Arya the Dog"/>

---
