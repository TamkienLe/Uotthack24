import constants

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
def extract_content(s):
    materials = dict.fromkeys(constants.MATERIALS)
    rn = ca = -1
    location = ''
    # Split line by line

    # Split each line by whitespace

    # Check if string is a key, if it is then next item is value
    # Check if each key has value followed immediately after without whitespace for edge cases
    # Special case for 'Made In'
    # Need to check previous element for material -> different than manufacturer
    
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

            print(val)

            if "RN" in val.upper():
                val = val.strip("RNrn#F")
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
                val = val.strip("CAca#F")
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

            


            prevWasRNKey = False
            prevWasCAKey = False
            prev = val



    print('Location is: ', location)
    print("RN is: ", rn)
    print("CA is: ", ca)


extract_content(testcase)