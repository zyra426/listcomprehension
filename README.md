# List Comprehension

List comprehension in Python offers a concise and readable way to create new lists from existing ones. It is a powerful tool that can be used in a variety of situations, such as filtering, mapping, and transforming data.

## But... Why?

Lists are a mutable data structure, meaning that they can be changed after they have been created. Often we need to create new lists based on existing ones but we don't want to change the original list or we may want to perform some operation on each element of a list and store the result in a new list.

Previously we may have done something like this:

```python
original_list = [1, 2, 3, 4, 5]
new_list = []

for num in original_list:
    new_list.append(num * 2)

print(new_list)  # Output: [2, 4, 6, 8, 10]
```

With list comprehension we can achieve the same result in a more concise way.

The syntax of list comprehension is as follows:

```python
new_list = [expression for item in original_list if condition]
```

The `expression` is the element or operation we want to perform on each element of the original list. In this case, we want to multiply each element by 2.

The `if` is optional. We will get to that later.

Taking the previous example, we can rewrite it as:

```python
original_list = [1, 2, 3, 4, 5]
new_list = [num * 2 for num in original_list]

print(new_list)  # Output: [2, 4, 6, 8, 10]
```

## And that condition?

The conditional at the end can be used if we want to filter the list based on some condition or perform some operation on an element only if that element satisfies a certain condition.

For example, if we want to filter the list based on whether the element is even or odd:

```python
original_list = [1, 2, 3, 4, 5]
new_list = [num for num in original_list if num % 2 == 0]

print(new_list)  # Output: [2, 4]
```

Or if we want to perform some operation only on the even elements:

```python
original_list = [1, 2, 3, 4, 5]
new_list = [num * 2 for num in original_list if num % 2 == 0]

print(new_list)  # Output: [4, 8]
```

## Assignment

Fantasy Quest has added a new Hunt feature for players who want more challenging fights. We want to keep track of who has completed a Hunt so we can display their character's name on a Hall of Fame board. Let's use list comprehension to achieve this!

Currently, we have a `List` of `Tuples` that contain the Hunt's `ID`, the player's `ID`, a boolean value representing whether the player has accepted the Hunt, and a boolean value representing whether the player has completed the Hunt.

Complete the `create_hall_of_fame` function to return a list of all the characters who have completed a Hunt.
