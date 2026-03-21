a = 20
B = 9
print(a + B)



"""
Dictionary examples and short exercises for learning.

Run this file to see concise examples for:
- Overview
- Creation & access
- Common methods
- Iteration
- Comprehensions
- Nesting & copying
- Use cases (Counter, defaultdict)
- Small exercises with sample outputs
"""

from collections import Counter, defaultdict
import copy


def overview():
    print('--- Overview ---')
    d = {'a': 1, 'b': 2}  # mapping of keys to values
    print('Example dict:', d)
    print('Keys must be hashable (e.g., strings, numbers, tuples).')


def creation_access_examples():
    print('\n--- Creation & Access ---')
    a = {'x': 10, 'y': 20}
    b = dict(z=30)
    empty = {}
    print('a:', a, 'b:', b, 'empty:', empty)

    # Access
    print("a['x']:", a['x'])
    print("a.get('nope') ->", a.get('nope'))
    print("a.get('nope', 0) ->", a.get('nope', 0))

    # Add / update
    a['z'] = 99
    a.update({'x': 11})
    print('After add/update a:', a)

    # Delete
    val = a.pop('y')
    print('popped y=', val, 'now a=', a)


def common_methods():
    print('\n--- Common Methods ---')
    d = {'a': 1, 'b': 2, 'c': 3}
    print('keys():', list(d.keys()))
    print('values():', list(d.values()))
    print('items():', list(d.items()))

    print("setdefault('d', 4) ->", d.setdefault('d', 4), 'd now', d)
    print("pop('a') ->", d.pop('a'))
    other = {'e': 5}
    d.update(other)
    print('after update:', d)
    d.clear()
    print('after clear:', d)


def iteration_examples():
    print('\n--- Iteration ---')
    d = {'one': 1, 'two': 2, 'three': 3}
    print('iterate keys:')
    for k in d:
        print(k, end=' ')
    print('\niterate values:')
    for v in d.values():
        print(v, end=' ')
    print('\niterate items:')
    for k, v in d.items():
        print(k, '->', v)

    print('\nSafe modification while iterating:')
    for k in list(d.keys()):
        if k.startswith('t'):
            d.pop(k)
    print('after removals:', d)


def comprehension_examples():
    print('\n--- Comprehensions ---')
    d = {'a': 1, 'b': 2, 'c': -1}
    doubled = {k: v * 2 for k, v in d.items()}
    positive = {k: v for k, v in d.items() if v > 0}
    print('doubled:', doubled)
    print('positive:', positive)


def nesting_copying_examples():
    print('\n--- Nesting & Copying ---')
    nested = {'outer': {'inner': 42}, 'list': [1, 2, 3]}
    shallow = nested.copy()
    deep = copy.deepcopy(nested)

    nested['outer']['inner'] = 99
    nested['list'].append(4)
    print('original after change:', nested)
    print('shallow (shares nested objects):', shallow)
    print('deep (independent):', deep)


def use_cases_best_practices():
    print('\n--- Use Cases & Best Practices ---')
    words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    freq = Counter(words)
    print('Counter freq:', freq)

    grouped = defaultdict(list)
    for w in words:
        grouped[w[0]].append(w)  # group by first letter
    print('grouped by first letter:', dict(grouped))


def exercises():
    print('\n--- Exercises (with implementations) ---')

    # 1. Word count
    def word_count(words):
        c = {}
        for w in words:
            c[w] = c.get(w, 0) + 1
        return c

    print('word_count:', word_count(['a', 'b', 'a', 'c', 'b', 'a']))

    # 2. Group by key function
    def group_by(items, keyfunc):
        out = {}
        for item in items:
            k = keyfunc(item)
            out.setdefault(k, []).append(item)
        return out

    items = ['apple', 'ape', 'banana', 'berry']
    grouped = group_by(items, lambda s: s[0])
    print('group_by first letter:', grouped)

    # 3. Merge dicts summing numeric values
    def merge_sum(d1, d2):
        out = d1.copy()
        for k, v in d2.items():
            out[k] = out.get(k, 0) + v
        return out

    print('merge_sum:', merge_sum({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))


if __name__ == '__main__':
    overview()
    creation_access_examples()
    common_methods()
    iteration_examples()
    comprehension_examples()
    nesting_copying_examples()
    use_cases_best_practices()
    exercises()

