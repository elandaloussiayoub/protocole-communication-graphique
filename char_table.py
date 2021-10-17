from string import ascii_lowercase, ascii_uppercase


lang = {}

# Numbers
for i in range(10):
  lang[str(i)] = i

# Alphabet
i = 10
for c in ascii_lowercase:
  lang[c] = i
  i+= 1

# Symbols
lang['.'] = 36
lang[','] = 37
lang[':'] = 38
lang[';'] = 39
lang['!'] = 40
lang['?'] = 41
lang['.'] = 42
lang['/'] = 43
lang['$'] = 44
lang['&'] = 45
lang['@'] = 46
lang[' '] = 47
lang['|'] = 48
lang['+'] = 49
lang['-'] = 50
lang['*'] = 51
lang['/'] = 52
lang['#'] = 53
lang['('] = 54
lang[')'] = 55

lang["'"] = 56
lang['~'] = 57
lang['%'] = 58
lang['^'] = 59
lang['{'] = 60
lang['}'] = 61
lang['['] = 62
lang[']'] = 63

# print(lang)