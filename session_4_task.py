# -*- coding: utf-8 -*-
"""session-4-task.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12egdM0BbtJId7nvephhMnUgIj-Ktshq1

###`Problem 1:` Combine two lists index-wise(columns wise)

Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

`Given List:`
```
list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]
```

`Output:`
```
[['M','y'], ['na', me'], ['i', 's'], ['Kh', 'an']]
```
"""

# Write code here

list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]

list(zip(list1,list2))



"""### `Problem 2:` Add new item to list after a specified item
Write a program to add item 7000 after 6000 in the following Python List
```
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
```
`Output:`
```
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
```
"""

# Write code here

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

(list1[2][2]).append(7000)

list1

"""###`Problem 3:` Update no of items available

Suppose you are given a list of candy and another list of same size representing no of items of respective candy.

i.e -  
```
candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]
```

Write a program to show no. of items of each candy type.

`Output:`

```
Jelly Belly-10
Kit Kat-20
Double Bubble-34
Milky Way-74
Three Musketeers-32

```
"""

# Write code here

candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]
my_list = []

for i in candy_list:
  print(my_list.append(candy_list))

"""###`Problem 4:` Running Sum on list
Write a program to print a list after performing running sum on it.

i.e:

`Input:`
```
list1 = [1,2,3,4,5,6]
```
`Output:`
```
[1,3,6,10,15,21]
```
"""

# Write code here

"""###`Problem 5:` You are given a list of integers. You are asked to make a list by running through elements of the list by adding all elements greater and itself.

i.e. Say given list is `[2,4,6,10,1]`
resultant list will be `[22,20,10,23]`.

For 1st element `2` ->> these are greater `(4+6+10)` values and `2` itself so on adding becomes `22`.

For 2nd element `4` ->> greater elements are `(6, 10)` and `4` itself, so on adding `20`

like wise for all other elememts.

`[2,4,6,10,1]`-->`[22,20,16,10,23]`



"""

# Write code here

"""###`Problem 6:` Find list of common unique items from two list. and show in increasing order

`Input`

```
num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]
```

`Output:`
```
[34, 67, 89]
```

"""

# Write code here

"""###`Problem 7:` Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.

`Input:`
```
['1ac21', '23fg', '456', '098d','1','kls']
```

`Output:`
```
['456', '23fg', '1ac21', '1', 'kls', '098d']

```
"""

# Write code here

"""`Problem 8:` Split String of list on K character.

**Example :**

Input:
```bash
['CampusX is a channel', 'for data-science', 'aspirants.']
```

Output:
```bash
['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']
```
"""

# Write code here

"""### `Problem 9:` Convert Character Matrix to single String using string comprehension.

**Example 1:**

Input:
```bash
[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
```

Output:
```bash
campux is best channel
```
"""

# Write code here

"""### `Problem 10:` Add Space between Potential Words.

**Example:**

Input:

```bash
['campusxIs', 'bestFor', 'dataScientist']
```

Output:
```bash
['campusx Is', 'best For', 'data Scientist']
```
"""

# Code here

"""### `Problem 11:` Write a program that can perform union operation on 2 lists

**Example:**

Input:

```bash
[1,2,3,4,5,1]
[2,3,5,7,8]
```

Output:
```bash
[1,2,3,4,5,7,8]
```
"""

# Write code here

"""### `Problem 12:` Write a program that can find the max number of each row of a matrix

**Example:**

Input:

```bash
[[1,2,3],[4,5,6],[7,8,9]]
```

Output:
```bash
[3,6,9]
```
"""

# Write code here

"""### `Problem 13:` Write a list comprehension to print the following matrix

[[0, 1, 2], [3, 4, 5], [6, 7, 8]]
"""

# Write code here

"""### `Problem 14:` Write a list comprehension that can transpose a given matrix

matrix = [<br>
  [1,2,3],<br>
          [4,5,6],<br>
          [7,8,9]<br>]<br>

[1, 4, 7]<br>
[2, 5, 8]<br>
[3, 6, 9]<br>
"""

# Write code here

"""### `Problem 15:` Write a list comprehension that can flatten a nested list

Input<br>
matrix = [<br>
  [1,2,3],<br>
          [4,5,6],<br>
          [7,8,9]<br>]<br>

Output:<br>
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

# Write code here