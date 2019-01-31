# ===================================== 25/5/2018 ===================================== #
mylist = [(20, 'Start', '2008-10-10', 'TBS'), (20, 'End', '2008-11-09', 'NG'),
          (21, 'Start', '2008-12-10', 'TBS'), (21, 'End', '2008-12-15', 'G'),
          (22, 'Start', '2009-01-10', 'TBS'), (22, 'End', '2009-12-10', 'B')]

code = 0
brr = []
for row in mylist:
    if row[1] == "Start":
        arr = []
        code = row[0]
        arr.extend((row[0], row[1], row[2]))
        continue

    if row[0] == code and row[1] == "End":
        arr.extend((row[1], row[2], row[3]))
    brr.append(arr)
for k in brr:
    print(k)

# FIXED: replaced .append by .extend (...) -1 for voting for myself
# ====================================================================================== #
