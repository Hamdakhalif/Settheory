def set_theory_operations(set1, set2):
    # Display the input sets
    print("Set 1:", set1)
    print("Set 2:", set2)

    # Union of sets
    union_result = set1.union(set2)
    print("\nUnion of sets:", union_result)

    # Intersection of sets
    intersection_result = set1.intersection(set2)
    print("Intersection of sets:", intersection_result)

    # Difference of sets (elements in set1 but not in set2)
    difference_result_1 = set1.difference(set2)
    print("Difference (Set 1 - Set 2):", difference_result_1)

    # Difference of sets (elements in set2 but not in set1)
    difference_result_2 = set2.difference(set1)
    print("Difference (Set 2 - Set 1):", difference_result_2)

    # Symmetric difference of sets (elements in either set but not in both)
    symmetric_difference_result = set1.symmetric_difference(set2)
    print("Symmetric Difference of sets:", symmetric_difference_result)


if __name__ == "__main__":
    # Example sets
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}

    # Perform set theory operations
    set_theory_operations(set_a, set_b)
