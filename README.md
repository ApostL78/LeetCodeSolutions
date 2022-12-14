# Run with Docker

To run all tests without cloning repository you can use `docker` ([install](https://www.docker.com/) before usage) with
following command:

  ```commandline
docker pull apostl/leetcode-solutions:latest
```

Then run pulled image:

```commandline
docker run apostl/leetcode-solutions:latest
```

# Expected result

After running the image you will see the result of running all tests in console:

```shell
============================= test session starts ==============================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /app, configfile: pytest.ini
collecting ... collected 170 items

.....

============================= 170 passed in 2.00s ==============================
```

Listing containers must show 0 containers running:

```shell
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                    NAMES
```

But in list of all containers you can see 1 container:

```shell
$ docker ps -a
CONTAINER ID   IMAGE                              COMMAND        CREATED          STATUS                     PORTS     NAMES
9d2438f4c558   apostl/leetcode-solutions:latest   "pytest -vv"   11 seconds ago   Exited (0) 7 seconds ago             frosty_bartik
```

# Python Solutions for LeetCode

| №      | Title                                                                                                                                                                       |                                                                         Solution                                                                          |                        Complexity                        |                                                        Best Tries                                                        |
|:-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| `217`  | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)                                                                                                     |                          [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/217_Contains_Duplicate.py)                           |   ***Time:***         `O(n)`<br/> ***Space:*** `O(1)`    |  `Runtime:` `475 ms`***,*** ***faster than*** `91.62%` <br/> `Memory Usage:` `25.9 MB`***,*** ***less than*** `67.10%`   |
| `69`   | [Sqrt(x)](https://leetcode.com/problems/sqrtx/)                                                                                                                             |                                [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/69_Sqrt(x).py)                                 | ***Time:***         `O(log(n))`<br/> ***Space:*** `O(1)` |  `Runtime:`  `33 ms`***,*** ***faster than*** `97.69%` <br/> `Memory Usage:` `13.7 MB`***,*** ***less than*** `95.90%`   |
| `14`   | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)                                                                                               |                         [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/14_Longest_Common_Prefix.py)                          |       ***Time:*** `O(n)`<br/> ***Space:*** `O(1)`        |  `Runtime:`  `33 ms`***,*** ***faster than*** `96.61%` <br/> `Memory Usage:` `13.9 MB`***,*** ***less than*** `88.41%`   |
| `2095` | [Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)                                                           |               [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/2095_Delete_the_Middle_Node_of_a_Linked_List.py)                |       ***Time:*** `O(n)`<br/> ***Space:*** `O(1)`        | `Runtime:`  `1778 ms`***,*** ***faster than*** `97.45%` <br/> `Memory Usage:` `59.1 MB`***,*** ***less than*** `98.65%`  |
| `24`   | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)                                                                                                   |                          [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/24_Swap_Nodes_in_Pairs.py)                           |       ***Time:*** `O(n)`<br/> ***Space:*** `O(1)`        |  `Runtime:`  `31 ms`***,*** ***faster than*** `95.39%` <br/> `Memory Usage:` `13.8 MB`***,*** ***less than*** `97.39%`   |
| `328`  | [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)                                                                                                 |                         [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/328_Odd_Even_Linked_List.py)                          |       ***Time:*** `O(n)`<br/> ***Space:*** `O(1)`        |  `Runtime:`  `47 ms`***,*** ***faster than*** `91.67%` <br/> `Memory Usage:` `16.5 MB`***,*** ***less than*** `98.89%`   |
| `1721` | [Swapping Nodes in a Linked List](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/)                                                                           |                   [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/1721_Swapping_Nodes_in_a_Linked_List.py)                    |       ***Time:*** `O(n)`<br/> ***Space:*** `O(1)`        |  `Runtime:`  `951 ms`***,*** ***faster than*** `99.55%` <br/> `Memory Usage:` `48.3 MB`***,*** ***less than*** `95.97%`  |
| `1019` | [Next Greater Node In Linked List](https://leetcode.com/problems/next-greater-node-in-linked-list/)                                                                         |                   [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/1019_Next_Greater_Node_In_Linked_List.py)                   |       ***Time:*** `O(n)`<br/> ***Space:*** `O(n)`        |  `Runtime:`  `324 ms`***,*** ***faster than*** `93.52%` <br/> `Memory Usage:` `18.8 MB`***,*** ***less than*** `86.93%`  |
| `382`  | [Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/)                                                                                           |                        [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/382_Linked_List_Random_Node.py)                        |       ***Time:*** `O(n)`<br/> ***Space:*** `O(1)`        |  `Runtime:`  `98 ms`***,*** ***faster than*** `84.89%` <br/> `Memory Usage:` `17.1 MB`***,*** ***less than*** `96.85%`   |
| `445`  | [Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/submissions/)                                                                                         |                          [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/445_Add_Two_Numbers_II.py)                           |       ***Time:*** `O(n)`<br/> ***Space:*** `O(n)`        |  `Runtime:`  `69 ms`***,*** ***faster than*** `95.16%` <br/> `Memory Usage:` `13.7 MB`***,*** ***less than*** `99.45%`   |
| `817`  | [Linked List Components](https://leetcode.com/problems/linked-list-components/)                                                                                             |                        [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/817_Linked_List_Components.py)                         |       ***Time:*** `O(n)`<br/> ***Space:*** `O(n)`        |  `Runtime:`  `113 ms`***,*** ***faster than*** `93.74%` <br/> `Memory Usage:` `19.1 MB`***,*** ***less than*** `60.86%`  |
| `725`  | [Split Linked List in Parts](https://leetcode.com/problems/split-linked-list-in-parts/)                                                                                     |                      [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/725_Split_Linked_List_in_Parts.py)                       |       ***Time:*** `O(n)`<br/> ***Space:*** `O(n)`        |  `Runtime:`  `30 ms`***,*** ***faster than*** `99.83%` <br/> `Memory Usage:` `14.1 MB`***,*** ***less than*** `99.67%`   |
| `61`   | [Rotate List](https://leetcode.com/problems/rotate-list/)                                                                                                                   |                              [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/61_Rotate_List.py)                               |       ***Time:*** `O(n)`<br/> ***Space:*** `O(1)`        |  `Runtime:`  `28 ms`***,*** ***faster than*** `99.75%` <br/> `Memory Usage:` `13.8 MB`***,*** ***less than*** `98.91%`   |
| `2058` | [Find the Minimum and Maximum Number of Nodes Between Critical Points](https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/) | [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/2058_Find_the_Minimum_and_Maximum_Number_of_Nodes_Between_Critical_Points.py) |       ***Time:*** `O(n)`<br/> ***Space:*** `O(n)`        |  `Runtime:`  `1015 ms`***,*** ***faster than*** `96.30%` <br/> `Memory Usage:`  `54 MB`***,*** ***less than*** `97.69%`  |
| `148`  | [Sort List](https://leetcode.com/problems/sort-list/)                                                                                                                       |                               [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/148_Sort_List.py)                               |    ***Time:*** `O(nlog(n))`<br/> ***Space:*** `O(1)`     | `Runtime:`  `669 ms`***,*** ***faster than*** `87.44%` <br/> `Memory Usage:`  `36.4 MB`***,*** ***less than*** `90.87%`  |
| `2074` | [Reverse Nodes in Even Length Groups](https://leetcode.com/problems/reverse-nodes-in-even-length-groups/)                                                                   |                 [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/2074_Reverse_Nodes_in_Even_Length_Groups.py)                  |       ***Time:*** `O(kn)`<br/> ***Space:*** `O(1)`       | `Runtime:`  `2293 ms`***,*** ***faster than*** `88.36%` <br/> `Memory Usage:`  `53.5 MB`***,*** ***less than*** `93.65%` |
| `86`   | [Partition List](https://leetcode.com/problems/partition-list/)                                                                                                             |                             [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/86_Partition_List.py)                             |       ***Time:*** `O(n)`<br/> ***Space:*** `O(1)`        |  `Runtime:`  `32 ms`***,*** ***faster than*** `97.52%` <br/> `Memory Usage:`  `13.5 MB`***,*** ***less than*** `99.97%`  |
| `143`  | [Reorder List](https://leetcode.com/problems/reorder-list/)                                                                                                                 |                             [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/143_Reorder_List.py)                              |       ***Time:*** `O(n)`<br/> ***Space:*** `O(1)`        |  `Runtime:`  `91 ms`***,*** ***faster than*** `94.85%` <br/> `Memory Usage:`  `23.8 MB`***,*** ***less than*** `95.63%`  |
| `138`  | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)                                                                               |                     [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/138_Copy_List_with_Random_Pointer.py)                     |       ***Time:*** `O(n)`<br/> ***Space:*** `O(n)`        |  `Runtime:`  `24 ms`***,*** ***faster than*** `99.98%` <br/> `Memory Usage:`  `14.8 MB`***,*** ***less than*** `83.62%`  |
| `147`  | [Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/submissions/)                                                                                       |                          [Python](https://github.com/ApostL78/LeetCodeSolutions/blob/master/problems/147_Insertion_Sort_List.py)                          |      ***Time:*** `O(n^2)`<br/> ***Space:*** `O(1)`       | `Runtime:`  `941 ms`***,*** ***faster than***  `53.66%` <br/> `Memory Usage:`  `16.5 MB`***,*** ***less than*** `81.87%` |