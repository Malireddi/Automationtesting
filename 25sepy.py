# 1. Student Attendance Analysis
# A college maintains the daily attendance details of its students in the form of a list containing student IDs. Some students may have attended multiple sessions on the same day. The administration wants to identify the longest continuous sequence of sessions in which no student ID is repeated. Develop a solution that determines the maximum length of such a sequence.


def attendance(ids):
    last_seen={}
    
    left=0
    max_length=0
    
    for right in range(len(ids)):
        student_id=ids[right]
        
        if student_id in last_seen and last_seen[student_id]>=left:
            left=last_seen[student_id]+1
            
        last_seen[student_id]=right
        max_length=max(max_length,right-left+1)
        
    return max_length

ids=[1011,1015,1013,1012,1015,1015]

print(attendance(ids))



# 2. Online Shopping Price Analysis
# An online shopping application stores the prices of products viewed by a customer during a browsing session. The customer wants to identify a continuous range of products that provides the maximum possible total discount value. Given the discount values, determine the maximum value that can be obtained from any continuous range.

def max_discount(discounts):
    
    current_sum = discounts[0]
    max_sum = discounts[0]

    for i in range(1, len(discounts)):
        
        current_sum = max(discounts[i], current_sum + discounts[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

discounts = list(map(int, input().split()))

#input = 5 -1 2 4 1 3
print(max_discount(discounts))


# 3. Rainwater Collection System
# A city installs buildings of different heights along a straight road. During rainfall, water gets collected between taller buildings. The engineering team needs to calculate the total amount of water that can remain trapped after heavy rainfall based on the heights of the buildings.

def rain_water(height):
    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0
    water = 0

    while left < right:
        if height[left] <= height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water


height = list(map(int, input().split()))

print(rain_water(height))
            
            
            
# 4. Employee Performance Analysis
# A company stores the monthly performance scores of an employee for several months. The scores may contain both positive and negative values depending on the employee's performance. Management wants to identify the continuous period during which the employee achieved the highest overall performance.

def max_performance(scores):
    current_sum = scores[0]
    max_sum = scores[0]

    for i in range(1, len(scores)):
        current_sum = max(scores[i], current_sum + scores[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


scores = list(map(int, input().split()))

print(max_performance(scores))


# 5. Product Sales Analysis
# A retail company stores the daily sales quantity of a product for several consecutive days. Due to seasonal changes, some days may have negative adjustments. The company wants to identify the period that produced the highest multiplication of sales-related values. Develop a solution to determine this maximum product.

def max_product(sales):
    current_max = sales[0]
    current_min = sales[0]
    max_product = sales[0]

    for i in range(1, len(sales)):
        if sales[i] < 0:
            current_max, current_min = current_min, current_max

        current_max = max(sales[i], current_max * sales[i])
        current_min = min(sales[i], current_min * sales[i])

        max_product = max(max_product, current_max)

    return max_product


sales = list(map(int, input().split()))

print(max_product(sales))


# 6. Customer Purchase History
# An e-commerce application stores the product IDs purchased by a customer in chronological order. The same product may appear multiple times. The system needs to determine the longest sequence of consecutive purchases in which every product ID is unique.

def longest_unique(purchases):
    last_seen = {}
    left = 0
    max_length = 0

    for right in range(len(purchases)):
        product = purchases[right]

        if product in last_seen and last_seen[product] >= left:
            left = last_seen[product] + 1

        last_seen[product] = right
        max_length = max(max_length, right - left + 1)

    return max_length


purchases = list(map(int, input().split()))

print(longest_unique(purchases))



# 7. Bank Transaction Analysis
# A bank stores transaction amounts for a customer's account. A continuous group of transactions may add up to a specific target amount. The auditing system needs to determine how many different continuous transaction groups produce exactly the specified amount.
def count_subarrays(transactions, target):
    prefix_sum = 0
    count = 0
    frequency = {0: 1}

    for amount in transactions:
        prefix_sum += amount

        if prefix_sum - target in frequency:
            count += frequency[prefix_sum - target]

        frequency[prefix_sum] = frequency.get(prefix_sum, 0) + 1

    return count


transactions = list(map(int, input().split()))
target = int(input())

print(count_subarrays(transactions, target))


# 8. Employee Skill Grouping
# A company receives a list of employee skill codes represented as strings. Employees having the same set of characters in their skill codes belong to the same skill category, even if the characters appear in a different order. The HR system needs to organize employees into appropriate skill groups.
def group_skills(skills):
    groups = {}

    for skill in skills:
        key = ''.join(sorted(skill))

        if key not in groups:
            groups[key] = []

        groups[key].append(skill)

    return list(groups.values())


skills = input().split()

groups = group_skills(skills)

for group in groups:
    print(*group)

# 9. Network Packet Analysis
# A network monitoring system receives packet identifiers in chronological order. The system must determine the longest sequence of consecutive packets whose identifiers form a continuous numerical sequence, regardless of their original order in the incoming data.

def longest_consecutive(packets):
    packet_set = set(packets)
    max_length = 0

    for packet in packet_set:
        if packet - 1 not in packet_set:
            current = packet
            length = 1

            while current + 1 in packet_set:
                current += 1
                length += 1

            max_length = max(max_length, length)

    return max_length

packets = list(map(int, input().split()))

print(longest_consecutive(packets))

# 10. Hospital Appointment Scheduling
# A hospital receives appointment requests represented by starting and ending times. Some appointments overlap with each other. The scheduling system needs to combine overlapping appointment periods so that the final schedule contains only non-overlapping time ranges.

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort()

    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged


n = int(input())

intervals = []

for i in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

result = merge_intervals(intervals)

for interval in result:
    print(interval[0], interval[1])