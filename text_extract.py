import constants

gunk = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ#%'

testcase = '''
MADE IN CHINA
FABRIQUE EN CHINE
RNF 116442 
CA#56303
BODY/CORPS:
80% COTTON/COTON
20% POLYESTER
HOOD LINING/
DOUBLURE DE CAPUCHE
80% COTTON/COTON
20% POLYESTER
EXCLUSIVE OF DECORATION
SANS DECORATION
'''

testcase2 = '''
ADED
LONDON
DESIGNED IN LONDON
MADE IN CHINA
72% COTTON
20% VISCOSE
% POLYESTER
HAND WASH
NOT BEACH
TUNAL DAY
DO NOT OW
NOT DRY CLEAR
25 BAUMWOLLE
OR VISCOSE
6% POLYESTER
PANASON
SA
CREAT.
ZUN TROCK
PARECER
TAS COTON
4900
ten
EDEN
AUTRETEN
RESTER
MAINE
'''

def get_number(s):
    ret = 0
    try:
        ret = int(s)
    except:
        ret = -1
    
    return ret

# Algorithm to pull out a number from a string given some key
# May be multiple keys/numbers on one line
# numbers may not be split by whitespace

# Assumption is that at least CA and RN are seperated by whitespace, 
# same with made in and country
# country is one word
# Split line by line

# Split each line by whitespace

# Check if string is a key, if it is then next item is value
# Check if each key has value followed immediately after without whitespace for edge cases
# Special case for 'Made In'
# Need to check previous element for material -> different than manufacturer
def extract_content(s):
    materials = dict.fromkeys(constants.MATERIALS, 0)
    rn = ca = -1
    location = ''
    
    
    for line in s.split('\n'):
        # Handle location case
        if("MADE IN" in line.upper()):
            locationArr = line.split()
            location = locationArr[len(locationArr) - 1]
            continue
            
        prevWasRNKey = False
        prevWasCAKey = False
        prev = ''

        for val in line.split():
            val = val.strip()

            if "RN" in val.upper():
                val = val.strip(gunk)
                rnCandidate = get_number(val) 

                if rnCandidate > 0:
                    rn = rnCandidate
                    prev = val
                    continue

                prevWasRNKey = True
                prev = val
                continue
                
            if prevWasRNKey:
                rnCandidate = get_number(val) 

                if rnCandidate > 0:
                    rn = rnCandidate

            if "CA" in val.upper():
                val = val.strip(gunk)
                caCandidate = get_number(val) 

                if caCandidate > 0:
                    ca = caCandidate
                    prev = val
                    continue

                prevWasCAKey = True
                prev = val
                continue
                
            if prevWasCAKey:
                caCandidate = get_number(val) 

                if caCandidate > 0:
                    ca = caCandidate


            for material in constants.MATERIALS:
                if material in val:
                    percent = get_number(prev.strip(gunk))
                    materials[material] = percent if percent > 0 else materials[material]
                    
            prevWasRNKey = False
            prevWasCAKey = False
            prev = val

    ret = {
        "location": location,
        "RN": rn,
        "CA": ca,
        "materials": materials
    }

    return ret



print(extract_content(testcase))