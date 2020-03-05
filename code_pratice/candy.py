
def candy(num_candies, num_children):
    people = [0] * num_children
    give = 0
    while num_candies > 0:
        people[give % num_children] += min(give + 1, num_candies)
        give += 1
        num_candies -= give
    return people

print(candy(9,3))
