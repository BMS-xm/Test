def appearance(intervals):
#def appearance(intervals: dict[str, list[int]]) -> int:
    ls, le = intervals['lesson'][0], intervals['lesson'][1]
    s = 0
    interval_list = []
    for i in range(len(intervals['pupil']) // 2):
        ps, pe = intervals['pupil'][i * 2], intervals['pupil'][i * 2 + 1]
        for j in range(len(intervals['tutor']) // 2):
            ts, te = intervals['tutor'][j * 2], intervals['tutor'][j * 2 + 1]
            ints, inte = max(ls, ps, ts), min(le, pe, te)
            if ints < inte:
                interval_list.append([ints, inte])
    interval_list.sort(key=lambda x: x[0])
    t = 0
    for interval in interval_list:
        if interval[0] > t:
            s += interval[1] - interval[0]
            t = interval[1]
        else:
            if interval[1] > t:
                s += interval[1] - t
                t = interval[1]
    return s

tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
