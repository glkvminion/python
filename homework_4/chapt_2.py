import itertools

def generate_sequence(count, start=0, increment=1):
    sequence = []
    infinite_gen = itertools.count(start, increment)
    for _ in range(count):
        sequence.append(next(infinite_gen))
    return sequence

def apply_to_each(func, data):
    if isinstance(data, (list, tuple)):
        return type(data)(apply_to_each(func, element) if isinstance(element, (list, tuple)) else func(element) for element in data)
    return func(data)

def merge_iterables(*sources):
    return list(itertools.chain(*sources))

def flatten_iterables(source):
    return list(itertools.chain.from_iterable(source))

squared_merged = flatten_iterables(
    apply_to_each(lambda num: num**2, [generate_sequence(5, -10, 2.5), generate_sequence(3)])
)
print(squared_merged)

doubled_combined = apply_to_each(
    lambda num: num * 2, 
    merge_iterables(generate_sequence(5, -10, 2.5), generate_sequence(3), generate_sequence(10, 0, 5))
)
print(doubled_combined)

empty_flattened = flatten_iterables(
    apply_to_each(lambda num: num**2, [generate_sequence(0), generate_sequence(0)])
)
print(empty_flattened)

empty_doubled = apply_to_each(
    lambda num: num * 2, 
    merge_iterables(generate_sequence(0), generate_sequence(0), generate_sequence(0))
)
print(empty_doubled)
