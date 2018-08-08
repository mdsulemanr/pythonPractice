# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

# print 2 ** 10      # one kilobit, kb
# print 2 ** 10 * 8  # one kilobyte, kB

# print 2 ** 20      # one megabit, Mb
# print 2 ** 20 * 8  # one megabyte, MB

# print 2 ** 30      # one gigabit, Gb
# print 2 ** 30 * 8  # one gigabyte, GB

# print 2 ** 40      # one terabit, Tb
# print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).

def convert_seconds(number):
    h=int(number/3600)
    m=int((number%3600)/60)
    s=number%60

    time=''
    if h!=0:
        time+=str(h) + ' hours '
    else:
        time+=str(h) + ' hour '
    if m!=0:
        time+=str(m) + ' minutes '
    else:
        time+=str(m) + ' minute '
    if s!=0:
        time+=str(s) + ' seconds '
    else:
        time+=str(s) + ' second '

    return time


def download_time(filesize, fileUnit, BandWidth, BandWiddthUnit):
    if fileUnit[0]=='k':
        if fileUnit[1]=='b':
            size=filesize * 2 ** 10
        else:
            size=filesize * 2 ** 10 * 8
    elif fileUnit[0]=='M':
        if fileUnit[1]=='b':
            size=filesize * 2 ** 20
        else:
            size=filesize * 2 ** 20 * 8
    elif fileUnit[0]=='G':
        if fileUnit[1]=='b':
            size=filesize * 2 ** 30
        else:
            size=filesize * 2 ** 30 * 8
    else:
        if fileUnit[0]=='b':
            size=filesize * 2 ** 40
        else:
            size=filesize * 2 ** 40 * 8
    size = size * 1.0


    if BandWiddthUnit[0]=='k':
        if BandWiddthUnit[1]=='b':
            speed=BandWidth * 2 ** 10
            time=size/speed
        else:
            speed = BandWidth * 2 ** 10 * 8
            time = size / speed
    elif BandWiddthUnit[0]=='M':
        if BandWiddthUnit[1]=='b':
            speed = BandWidth * 2 ** 20
            time = size / speed
        else:
            speed = BandWidth * 2 ** 20 *8
            time = size / speed
    elif BandWiddthUnit[0]=='G':
        if BandWiddthUnit[1]=='b':
            speed = BandWidth * 2 ** 30
            time = size / speed
        else:
            speed = BandWidth * 2 ** 30 * 8
            time = size / speed
    else:
        if BandWiddthUnit[0]=='b':
            speed = BandWidth * 2 ** 40
            time = size / speed
        else:
            speed = BandWidth * 2 ** 40 * 8
            time = size / speed

    return convert_seconds(time)


print(download_time(1024, 'kB', 1, 'MB'))
# >>> 0 hours, 0 minutes, 1 second

print(download_time(1024, 'kB', 1, 'Mb'))
# >>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print(download_time(13, 'GB', 5.6, 'MB'))
# >>> 0 hours, 39 minutes, 37.1428571429 seconds

print(download_time(13, 'GB', 5.6, 'Mb'))
# >>> 5 hours, 16 minutes, 57.1428571429 seconds

print(download_time(10, 'MB', 2, 'kB'))
# >>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print(download_time(10, 'MB', 2, 'kb'))
# >>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

