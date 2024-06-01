# Numpy Assignment

## Questions

1. Create a 1D Numpy array with values from 0 to 9.




3. Create a Numpy array with values ranging from 10 to 49.


4. Create a 2D Numpy array and change the data type to float.


5. Create a 4x4 identity matrix.


6. Create a Numpy array with 10 values evenly spaced between 1 and 5.

7. Create a 3x3 Numpy array with random values.


8. Create a Numpy array with 20 random values and reshape it to a 4x5 array.


9. Create an array of shape (3, 3) and extract the values of the second row.

10. Create a 5x5 matrix with values 1 to 25 and extract the element in the third row and fourth column.

11. Find the shape, size, and data type of a given Numpy array.


12. Flatten a given 2D Numpy array.

13. Concatenate two Numpy arrays along the second axis.


14. Split a given Numpy array into 3 equal-sized sub-arrays.


15. Create a Numpy array with 10 random integers between 1 and 100, and find the maximum and minimum values.


16. Create a Numpy array with random values and replace all values greater than 0.5 with 1.


17. Multiply two given Numpy arrays element-wise.


18. Compute the dot product of two given Numpy arrays.

19. Add a scalar value to a given Numpy array.


20. Subtract one Numpy array from another.


21. Find the mean, median, and standard deviation of a given Numpy array.


22. Sort a given Numpy array along the first axis.


23. Find the unique elements of a given Numpy array.


24. Check if a given Numpy array contains any NaN values.


25. Create a 5x5 matrix and pad it with zeros along the border.

26. Transpose a given Numpy array.


27. Reverse the rows of a given 2D Numpy array.


28. Compute the cumulative sum of a given Numpy array.


29. Normalize a given Numpy array.


30. Reshape a given Numpy array to have 1 row and multiple columns.



## Answers

```python
# Answers to the questions
# 1. arr1 = np.arange(10)
# 2. arr2 = np.ones((3, 3), dtype=bool)
# 3. arr3 = np.arange(10, 50)
# 4. arr4 = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
# 5. arr5 = np.identity(4)
# 6. arr6 = np.linspace(1, 5, 10)
# 7. arr7 = np.random.random((3, 3))
# 8. arr8 = np.random.random(20).reshape(4, 5)
# 9. second_row = arr9[1, :]
# 10. element = arr10[2, 3]
# 11. shape = arr11.shape; size = arr11.size; dtype = arr11.dtype
# 12. flat_arr = arr12.flatten()
# 13. concatenated = np.concatenate((arr13_1, arr13_2), axis=1)
# 14. sub_arrays = np.split(arr14, 3)
# 15. max_value = np.max(arr15); min_value = np.min(arr15)
# 16. arr16[arr16 > 0.5] = 1
# 17. result = np.multiply(arr17_1, arr17_2)
# 18. dot_product = np.dot(arr18_1, arr18_2)
# 19. result = arr19 + 5
# 20. result = arr20_1 - arr20_2
# 21. mean = np.mean(arr21); median = np.median(arr21); std_dev = np.std(arr21)
# 22. sorted_arr = np.sort(arr22, axis=0)
# 23. unique_elements = np.unique(arr23)
# 24. has_nan = np.isnan(arr24).any()
# 25. padded_arr = np.pad(arr25, pad_width=1, mode='constant', constant_values=0)
# 26. transposed_arr = arr26.T
# 27. reversed_rows = arr27[::-1, :]
# 28. cumsum = np.cumsum(arr28)
# 29. normalized_arr = (arr29 - np.min(arr29)) / (np.max(arr29) - np.min(arr29))
# 30. reshaped_arr = arr30.reshape(1, -1)
