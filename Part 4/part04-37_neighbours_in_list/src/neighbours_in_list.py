# Write your solution here


def longest_series_of_neighbours(nums: list) -> int:
    tracker_total = 0
    tracker_helper = 1

    for i in range(len(nums)):
        print('index',i, '---','data',nums[i])
        
        if abs(nums[i] - nums[i - 1]) == 1:
            tracker_helper += 1
            # print(f'Previous number was {nums[i - 1]}. Number now is {nums[i]}. Difference is just one so the are neighboors')
            # print(f'increasing helper by 1. helper is now {tracker_helper}. Total remains unchaned for now {tracker_total}')
         

                
        else:
            # print(f'Previous number was {nums[i - 1]}. Number now is {nums[i]}. They ARE NOT neigboors')
            # print(f'Helper is {tracker_helper}. Total is {tracker_total}')
                      
            tracker_total = max(tracker_total, tracker_helper)
            # print(f'found a non neighboor. copying helper to total if helper is higher')

            tracker_helper = 1
            # print('total', tracker_total)
            # print('helper', tracker_helper)
                    

    tracker_total = max(tracker_total, tracker_helper)
    return tracker_total
            






if __name__ == '__main__' :
    
    print(longest_series_of_neighbours([0, 1, 2, 3, 4, 5, 9, 10, 11, 2, 3, 4]))
    # print(longest_series_of_neighbours([1, 2, 3, 0, 1, 2, 3, 4, 5, 3, 4, 5, 1, 2, 3]))
    # print(longest_series_of_neighbours([1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25, 30]))
    # print(longest_series_of_neighbours([5, 3, 4, 2, 3, 1, 2, 3, 9, 8, 7, 8, 7, 6, 7, 6]))