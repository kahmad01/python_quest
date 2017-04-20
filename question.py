""" Some python sample questions """
import argparse
import sys
import os


def fabonacci(start, next):
    """ start: start fab no
        next: till these many numbers
    """

    def fab(start):
        if start == 1 or start == 0:
            return 1
        else:
            return fab(start - 1) + fab(start - 2)

    fab_series = map(fab, range(1,next))
    return fab_series


def count_number_of_letters(mystr, typ=1):
    """Different typs available which one 
        to use
    """
    if typ == 1:
        return len(mystr.replace(" ", ""))
    elif typ == 2:
        return len(mystr) - mystr.count(" ")
    elif typ == 3:
        new_str = mystr.split()
        return len("".join(new_str))


def find_divisible(num=None, upto=None):
    """ Find the numbers divisible upto this limit
    """
    if num:
        if type(num) == "list":
            # assuming if list is not provided
            total_nums = [int(n) for n in num]
            num_list = [j for i in total_nums for j in range(1, len(upto + 1)) if j % i == 0]
            return num_list
        elif type(num) == "int":
            num_list = [i for i in range(1, len(upto + 1)) if i % num == 0]
            return num_list
    else:
        print "num: %s should be greater than 0 and not empty" % num
        sys.exit(1)


def factorial(n):
    """Find factorial of the number"""
    if n <= 0:
        print "n should be greater than 0"
        sys.exit(1)
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def find_files(src, filelist=None, dirlist=None):
    """ src : Path of the dir
        filelist: contains list of files
        dirlist: contains list of dirs
        All files and dirlist is recursive
    """
    list_dir = os.listdir(src)
    for f in list_dir:
        new_path = os.path.join(src, f)
        if os.path.isdir(new_path):
            dirlist.append(new_path)
            find_files(new_path)
        else:
            filelist.append(new_path)
    return filelist, dirlist


def find_sum_of_student(myfile, stname):
    """ find the sum of students name from record
        and print in file
    """
    records = {}
    try:
        with open(myfile, "r") as f:
            for st in f.readlines():
                per_st_record = st.splitlines(" ")
                if st not in records.keys():
                    st_name = per_st_record[0]
                    st_marks = int(per_st_record[-1])
                    records[st_name] = st_marks
                else:
                    records[st_name] += st_marks
    except Exception as e:
        print e
    return records[stname]


def construct_str(masterfile, substring):
    """ find the substring in the masterstring
    """
    substring = substring.split()
    set_substr = set(substring)
    with open(masterfile, "r") as f:
        master_set = set(f.read().split())
    if set_substr.issubset(master_set):
        print "All words found in given string"
        num_str = [w for w in set_substr if w in master_set]
    return num_str


def find_count(masterstr, substr):
    """find the count of substr in masterstr
	"""
    count = 0
    for i in range(len(masterstr)):
        if masterstr[i:i + len(substr)] == substr:  # This is the key
            count += 1
    return count


def sort_list(data_list):
    #	ex: data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
    new_list = []

    while data_list:
        minimum = data_list[0]  # arbitrary number in list
        for x in data_list:
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        data_list.remove(minimum)

    return new_list


#agrs,l = argparse.ArgumentParser("Choose a method to be picked")
#("--method", destination=method, type=string, help="Function name to execute. Pick from ")
mstr="CDCDCDCDCDCDACDCD"
stm="CDC"
print find_count(mstr,stm)
