
#did Eng-Spn to help with
#translations at school

eng2spn = {}
eng2spn['pretest'] = 'prueba preliminar'
eng2spn['sheet'] = 'la hoja'
eng2spn['learning target'] = 'objetivo de aprendizaje'
eng2spn['match it'] = 'compárelo'
eng2spn['were you'] = 'estuviste'
eng2spn['fingers'] = 'dedos'
eng2spn['keep'] = 'Mantén'

#delete key-value 

rosters = {'701class':30, '702class':35, '703class':25, '704class':6}
for akey in rosters.keys():  
    print("Got key", akey, "which maps to value", rosters[akey])
#output
#Got key 701class which maps to value 30
#Got key 702class which maps to value 35
#Got key 703class which maps to value 25
#Got key 704class which maps to value 6


cr = list(rosters.keys())       # Make a list of all of the keys
print(cr)
print(cr[3]) 

#['701class', '702class', '703class', '704class']
#704class
