def make_dictionary(keys, values):
    return dict(zip(keys, values))

if __name__ == '__main__':
    students = ["alice", "bob", "carol"]
    ids = frozenset([123, 124, 125])
    records = make_dictionary(ids, students)
    assert records == {123: 'alice', 124: 'bob', 125: 'carol'}
    print(records)
