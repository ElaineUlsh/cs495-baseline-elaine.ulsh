import re 
import unittest 

def normalize_and_count(s, token): 
    ns = s.lower() 
    ns = re.sub(r'[^\w\s]', '', ns) 
    tokens = ns.split() 
    
    return tokens.count(token.lower())