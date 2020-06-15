#!/usr/bin/python2.7
import re

def the_bucket_challenge(bucket_one,bucket_two,desired_bucket,starting=(0,0)):
    """This is the DieHard 3 Water Jug Problem, also known as the classic Water
    Pouring Problem. Here we explore different paths to reach a solution. We store each path
    in the variable explored. We store the order of the paths in frontier."""  
    if desired_bucket in starting:
        return [starting]
    explored = set() 
    frontier = [[starting]] 
    while frontier:
        path = frontier.pop(0)
        (x,y) = path[-1] #Last state in the first path of the frontier
        for (state, action) in successors (x,y,bucket_one,bucket_two).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action,state]
                #print(path2)
                if desired_bucket in state:
                    path_on_individual_lines = re.split('\),',str(path2))
                    steps = 0
                    for step_string in path_on_individual_lines:
                        steps += 1
                        if steps == 1:
                            step_string_without_parens = (step_string.replace('[(','')).split(',')
                            step_string_with_gallons ='Start with ' + step_string_without_parens[0]  + ' gallons in Bucket One and' + step_string_without_parens[1] + ' gallons in Bucket Two. All water is in the lake.'
                            print(step_string_with_gallons)
                        else:
                            step_string_without_quotes = step_string.replace('\'','')
                            step_string_without_parens = ((step_string_without_quotes.replace('(','')).replace(')]','')).split(',')
                            step_string_with_gallons = ('Step ' + str(steps - 1) + ': ' + str(step_string_without_parens[0]) + ' --> Bucket One has' + str(step_string_without_parens[1]) + ' gallons. Bucket Two has' + str(step_string_without_parens[2]) + ' gallons.' )
                            print(step_string_with_gallons)
                    #print(path2)    
                    return path2
                else:
                    frontier.append(path2)
    
    return Fail 
    
Fail = []


def successors(x,y,bucket_one,bucket_two):
    """ These are notes about x and y:
    x = level of bucket one
    y = level of bucket two
    """
    
    assert x <= bucket_one and y <= bucket_two 
    return {((0,y+x) if y+x<=bucket_two else (x-(bucket_two-y), y+(bucket_two-y))): 'Pour bucket one into bucket two',
            ((x+y, 0) if x+y<=bucket_one else (x+(bucket_one-x), y-(bucket_one-x))): 'Pour bucket two into bucket one',
            (bucket_one,y): 'Fill bucket one with ' + str(bucket_one) + ' gallons' , (x,bucket_two):'Fill bucket two with ' + str(bucket_two) + ' gallons',
            (0,y): 'Empty bucket one', (x,0):'Empty bucket two'}


bucket_one = int(raw_input('How many gallons are in your first bucket? '))
bucket_two = int(raw_input('How many gallons are in your second bucket? '))
desired_bucket = int(raw_input('How many gallons are in your desired bucket? '))
print('\n')


solution = the_bucket_challenge(bucket_one,bucket_two,desired_bucket)

if solution != Fail:
    print('Solution found.')
else:
    print('No solution possible.')
    


