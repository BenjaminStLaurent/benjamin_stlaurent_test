import sys

'''
Input: versionA => string (alphanum separated by '.')
       versionB => string (alphanum separated by '.')
       
Test cases:

1.2 1.2 => 1.2 is equal to 1.2
2.0 1.0 => 2.0 is greater than 1.0
1.0 2.0 => 2.0 is greater than 1.0
1.2.3.4 1.2.3 => 1.2.3.4 is greater than 1.2.3
1.2.1a 1.2.1b => 1.2.1b is greater than 1.2.1a
a.b a.b.c => a.b.c is greater than a.b

I'm assuming the inputs are valid

'''


def check_versions(version_a, version_b):
    values_a = version_a.split('.')
    values_b = version_b.split('.')

    while len(values_a) > 0 and len(values_b) > 0:
        val_a = values_a.pop(0)
        val_b = values_b.pop(0)

        if val_a > val_b:
            return "{} is greater than {}".format(version_a, version_b)
        if val_b > val_a:
            return "{} is less than {}".format(version_a, version_b)

    if len(values_a) > 0:
        return "{} is greater than {}".format(version_a, version_b)
    elif len(values_b) > 0:
        return "{} is less than {}".format(version_a, version_b)

    return "{} is equal to {}".format(version_a, version_b)


versionA = sys.argv[1]
versionB = sys.argv[2]

print(check_versions(versionA, versionB))

