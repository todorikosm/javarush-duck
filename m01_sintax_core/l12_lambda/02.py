import calendar

print(*[elem for elem in dir(calendar) if not elem.startswith('_')], sep='\n')