# https://leetcode.com/problems/interval-list-intersections/
# https://leetcode.com/problems/merge-intervals/

'''
Sample Input:
[['9:00’, ’10:30’], [’12:00’, ’13:00’], [’16:00’, ’18:00’]]
[[’10:00’, ’11:30’], [’12:30’, ’14:30’], [’14:30’: ’15:00’], [’16:00’, ’17:00’]]
Start = 10:00
End = 18:30
Meeting duration= 30

Sample output = [[’11:30’, ’12:00’], [’15:00’, ’16:00’], [’18:00’, ’18:30’]]
[[900, 1030], [1200, 1300], [1600, 1800]]
[[1000, 1130], [1230, 1330], [1430, 1500], [1600, 1700]]


'''
# find free times per person
# ['9:00’, ’10:30’], [’12:00’, ’13:00’], [’16:00’, ’18:00’]]
# free_time = [10:30-12:00]
def free_time(array_of_times, final_time):
    free_time = [] # [[10:30, 1200], [1300, 1600], ]
    
    len_times = len(array_of_times)
    first_time = array_of_times[0]
    end = first_time[1]    # 10:30

    # loop through start, end
    for i in range(1, len_times):
        curr_time = array_of_times[i]
        start = curr_time[0] # 1600 --> 12:00
        if start > end: # 1600 > 1300 --> 12 > 1030
            free_time.append([end, start])
        end = curr_time[1] # 18:00

    # address if last end is before close of day
    if end > final_time:
        free_time.append(end, final_time)
    
    return free_time
        
# 12:00 is after 10:30, 10:30-12:00. is fre time
    # end 

# may need to consider beinging of day start time later
# Meeting duration= 30
# give All overlapping free times
def compare_free_times(person1_times, person2_times):
    # p1: [[1130, 1200], [1300, 1600], [1800, 1830]]
    # p2: [[1030, 1300], [1500-1600]]
    
    joint_free_times = []
    
    # THESE ARE THE FREE TIMES
    len1 = len(person1_times) # 3
    len2 = len(person2_times) # 2
    
    p1 = 0
    p2 = 0
   
    # same times
    # check off by one
    while p1 > len1 and p2 > len2:
        start1 = person1_times[p1][0]
        start2 = person1_times[p2][0]
        end1 = person1_times[p1][1] # 1200
        end2 = person1_times[p2][1] # 1300
        if start1 == start2:
            if end1 > end2:
                joint_free_tmies.append(start1, end2)
            else:
                joint_free_tmies.append(start1, end1)
            p1 += 1
            p2 += 1
        # start1 first
        elif start1 < start2:
            end1 < start2:
                p1 += 1
            end1 >= start2: #1300, 1200
                if end2 < end1:
                    joint_free_time.append(start2, end2)
                    p2 += 1 
                else: # end2 is after end1
                    # start1 : 1000
                    # start2 : 1100
                    # end1 :   1200
                    # end2 :   1300
                    #1100, 1200 
                    joint_free_time.append(start2, end1)
                    p1 += 1      
        # start2 first
        else: # start1 > start2: # 1200, 1000
            # start1 : 1200
            # start2 : 1100
            # end1 :   1230
            # end2 :   1200
            #1100, 1200 
            # check ends 1230, 1300
            if end1 > end2: #1200, 1200
                # no free time
                p2 += 1
            else: # end1 < end2:
                # start1 : 1200
                # start2 : 1100
                # end1 :   1230
                joint_time.append(start1, end1)
                p1 += 1
    return joint_time
