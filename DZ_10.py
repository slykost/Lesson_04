s = input()
count = s.count('h', s.find('h') + 1, s.rfind('h'))
print(s[:s.find('h') + 1] + s[s.find('h') + 1:s.rfind('h')].replace('h', 'H', count) + s[s.rfind('h')])