nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

def flat_generator(a: list):
  for sublist in a:
    for item in sublist:
      yield item
  
for item in  flat_generator(nested_list):
    print(item)

