def camelcase(s):
    return ''.join([word.capitalize() for word in s.split('_')])


print(camelcase('some_string'))


# Output:  SomeString
