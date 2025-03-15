/*
We want to extend the array class so that it provides a contains_all? method. This method will always assume that an array is passed in and will return true if all values in the passed in array are present within the current array.

For example:

items = std::vector<int>{1, 2, 3, 4, 5, 6, 7, 8, 9}

contains_all(items, {1, 2, 3})  # should == true
contains_all(items, {1, 5, 13}) # should == false because 13 is not in the items array
ArraysFundamentals
*/