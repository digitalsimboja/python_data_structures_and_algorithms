# Patterns of Data structures and algorithms

## The sliding window problem is the shifting window pattern

The window starts from the head and shift based on the size of the window.
Also the size of the window might grow or shrink depending on the type of the problem.

### Scenario

- You’re asked to find the longest/shortest substring, subarray, or a desired value
- Linear data structures such as Linked lists, arrays or strings

### Examples

- Maximum sum subarray of size 'k' from a linked list
- Longest substring with 'k' distinct characters
- String Anagrams

## Two pointers

The pointers start from the head or tail and the move a step forward or backward

### Scenario

- Deal with sorted arrays that require to find element that fulfill a certain constraint
- Set of elements in the array is a pair, a triplet or even a subarray

### Examples

- squaring a sorted arrays
- compare strings that contain back space
- find the nth element from the last of linked list
- triplets that contain sum to zero

## Fast and slow pointers (Hare and Tortoise)

Just like the two-pointer algorithm but in this case, One pointer moves faster than the other.
Used for circular linked list. By moving at different speeds (say, in a cyclic linked list), the algorithm proves that the two pointers are bound to meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.

### Scenario

There are some cases where you shouldn’t use the Two Pointer approach such as in a singly linked list where you can’t move in a backwards direction. An example of when to use the Fast and Slow pattern is when you’re trying to determine if a linked list is a palindrome.

### Example cases

- Linked List Cycle (easy)
- Palindrome Linked List (medium)
- Cycle in a Circular Array (hard)

## Merge Intervals

### Scenario

If you’re asked to produce a list with only mutually exclusive intervals
If you hear the term “overlapping intervals”.

### Example cases

- Merge interval problem patterns:
- Intervals Intersection (medium)
- Maximum CPU Load (hard)

## Cyclic sort

### Scenario

They will be problems involving a sorted array with numbers in a given range
If the problem asks you to find the missing/duplicate/smallest number in an sorted/rotated array

### Example cases

- Find the Missing Number (easy)
- Find the Smallest Missing Positive Number (medium)

## In-place reversal of linked list

### Scenario
If you’re asked to reverse a linked list without using extra memory

### Example cases
- Reverse a Sub-list (medium)
- Reverse every K-element Sub-list (medium)