# Roller Coaster

You have been appointed to oversee and analyze the operations of a newly established amusement park. Your primary task is to predict the daily earnings for the park's roller coaster attraction. To do this, you must understand the rules and dynamics of how visitors queue for and ride the roller coaster.

### Rules and Operation

1. **Attraction Popularity:** The roller coaster is immensely popular, with visitors eager to experience multiple rides consecutively.

2. **Queue Formation:** Visitors queue up in front of the roller coaster attraction, either individually or in groups. Groups in the queue insist on riding together and cannot be separated.

3. **No Overtaking:** Visitors in the queue never overtake each other, maintaining their original order.

4. **Limited Attraction Capacity:** The roller coaster has a limited number of available seats, denoted as 'L.' 

5. **Attraction Operation Limit:** The roller coaster can only operate a fixed number of times per day, denoted as 'C.'

6. **Queue Size:** The queue is composed of 'N' groups of visitors, each group having a specific number of people ('Pi').

7. **Ticket Price:** Each individual visitor pays 1 dirham per ride.

### Attraction Earnings Calculation Example:
Let's consider an example with L=3, C=3, and 4 groups in the queue (N=4) with the following group sizes: [3, 1, 1, 2].

- **Ride 1:** On the first roller coaster ride, only the first group (size 3) can get on and fills all available seats. After the ride, this group returns to the back of the queue, which now looks like this: [1, 1, 2, 3]. Earnings from the ride: 3 dirhams.

- **Ride 2:** For the second ride, the next two single-person groups can get on, leaving one seat empty (as the following group of 2 people cannot be separated). After the ride, they return to the back of the queue: [2, 3, 1, 1]. Earnings from the ride: 2 dirhams.

- **Ride 3:** On the last ride (C=3), only the group of 2 people can get on, leaving one seat empty. Earnings from the ride: 2 dirhams.

**Total Earnings:** The total earnings for the day are the sum of the earnings from each ride: 3 + 2 + 2 = 7 dirhams.

### Your Task
Your mission is to develop a system that can estimate the daily earnings for the roller coaster attraction, given the values of L, C, and the queue sizes (N) for each group. You need to account for the rules and dynamics described to determine the total earnings for the day.

**Input:**
- L (the number of available seats on the roller coaster).
- C (the number of times the roller coaster can operate per day).
- N (the number of groups in the queue).
- An array representing the size of each group (Pi).

**Output:**
- The total earnings for the day, calculated based on the rules described.

Solve this problem to help the amusement park plan its daily operations and revenue projections for the roller coaster attraction.
