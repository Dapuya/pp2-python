s = input()
d = { 'SUN' : 7,
      'MON' : 6,
      'TUE' : 5,
      'WED' : 4,
      'THU' : 3,
      'FRI' : 2,
      'SAT' : 1
    }

if s in d.keys():
    print(d[s])
