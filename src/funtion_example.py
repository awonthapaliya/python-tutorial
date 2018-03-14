'''
Created on Mar 9, 2018

@author: awon
'''

# define functions using "def" key word
# No need to define return value to function'

def check_exist(countries):
    check_country = ['nepal', 'usa', 'Japan']
    for country in countries:
     if country.lower() in check_country:
        print 'Country found!!'       


def check_substring(string, substring):
      return substring in string


check_exist(['Australia', 'USA', 'Japan'])

print check_substring('Awon Thapaliya', 'Awon')
