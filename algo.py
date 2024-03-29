from math import cos, asin, sqrt, pi
import json
import requests
from bs4 import BeautifulSoup


url = "https://ised-isde.canada.ca/app/cb/can/public/cmpnyDtls.json?cano="

def algo(scan):
    # country of origin
    coa = scan["location"]

    cotton = scan["materials"]["COTTON"]
    polyester = scan["materials"]["POLYESTER"]
    nylon = scan["materials"]["NYLON"]
    silk = scan["materials"]["SILK"]
    wool = scan["materials"]["WOOL"]
    linen = scan["materials"]["LINEN"]
    fabric = scan["materials"]["ACRYLIC FABRIC"]

    rating = {
        'Finisterre' : 99,
        'People Tree' : 99,
        'School Uniform Shop' : 93,
        'Seasalt' : 80,
        'Patagonia' : 79,
        'Fat Face' : 77,
        'Whistles' : 73,
        'Monsoon Accessorize' : 70,
        'Phase Eight' : 70,
        'ASOS' : 67,
        'Crew Clothing' : 67,
        'Evans' : 67,
        'Miss Selfridge' : 67,
        'Topman' : 67,
        'Topshop' : 67,
        'French Connection' : 60,
        'New Look' : 60,
        'River Island' : 60,
        'Bershka' : 53,
        'Gap' : 53,
        'Joules' : 53,
        'Marks & Spencer' : 53,
        'Next' : 53,
        'Pull&Bear' : 53,
        'Stradivarius' : 53,
        'The North Face' : 53,
        'White Stuff' : 53,
        'Zara' : 53,
        'Fila' : 50,
        'Mango' : 50,
        '& Other Stories' : 48,
        'H&M' : 48,
        'Monki' : 48,
        'F&F at Tesco' : 47,
        'Primark' : 47,
        'Tommy Hilfiger' : 47,
        'Tu at Sainsburys' : 47,
        'adidas' : 41,
        'Matalan' : 38,
        'Boohoo' : 37,
        'Burton' : 37,
        'Coast' : 37,
        'Dorothy Perkins' : 37,
        'Nasty Gal' : 37,
        'Nike' : 37,
        'Oasis' : 37,
        'Pretty Little Thing' : 37,
        'Wallis' : 37,
        'Warehouse' : 37,
        'George at Asda' : 32,
        'I Saw It First' : 30,
        'Missguided' : 30,
        'Shein' : 29,
        'Uniqlo' : 59
    }
    
    if (scan["CA"] != -1):
        page = requests.get(url + str(scan["CA"]))

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find("div", {"class": "col-sm-8"})
        results = results.prettify().split("\n")[1]
        brand = results.strip()
        brand_score = 0

        for k, v in rating.items():
            if k.lower() in brand.lower(): brand_score = v
    else: brand_score = -1

    makeup = {}

    if cotton != 0: makeup["cotton"] =  cotton
    if polyester != 0: makeup["polyester"] =  polyester
    if nylon != 0: makeup["nylon"] =  nylon
    if silk != 0: makeup["silk"] =  silk
    if wool != 0: makeup["wool"] =  wool
    if linen != 0: makeup["linen"] =  linen
    if fabric != 0: makeup["fabric"] =  fabric

    # contains latitude and longitude of all countries to
    countries = {
        'afghanistan' : ['34.28N','69.11E'],
        'albania' : ['41.18N','19.49E'],
        'algeria' : ['36.42N','03.08E'],
        'american samoa' : ['14.16S','170.43W'],
        'andorra' : ['42.31N','01.32E'],
        'angola' : ['08.50S','13.15E'],
        'antigua and barbuda' : ['17.127N','61.846W'],
        'argentina' : ['36.30S','60.00W'],
        'armenia' : ['40.10N','44.31E'],
        'aruba' : ['12.32N','70.02W'],
        'australia' : ['35.15S','149.08E'],
        'austria' : ['48.12N','16.22E'],
        'azerbaijan' : ['40.29N','49.56E'],
        'bahamas' : ['25.05N','77.20W'],
        'bahrain' : ['26.10N','50.30E'],
        'bangladesh' : ['23.43N','90.26E'],
        'barbados' : ['13.05N','59.30W'],
        'belarus' : ['53.52N','27.30E'],
        'belgium' : ['50.51N','04.21E'],
        'belize' : ['17.18N','88.30W'],
        'benin' : ['06.23N','02.42E'],
        'bhutan' : ['27.31N','89.45E'],
        'bolivia' : ['16.20S','68.10W'],
        'bosnia and herzegovina' : ['43.52N','18.26E'],
        'botswana' : ['24.45S','25.57E'],
        'brazil' : ['15.47S','47.55W'],
        'british virgin islands' : ['18.27N','64.37W'],
        'brunei darussalam' : ['04.52N','115.00E'],
        'bulgaria' : ['42.45N','23.20E'],
        'burkina faso' : ['12.15N','01.30W'],
        'burundi' : ['03.16S','29.18E'],
        'cambodia' : ['11.33N','104.55E'],
        'cameroon' : ['03.50N','11.35E'],
        'canada' : ['45.27N','75.42W'],
        'cape verde' : ['15.02N','23.34W'],
        'cayman islands' : ['19.20N','81.24W'],
        'central african republic' : ['04.23N','18.35E'],
        'chad' : ['12.10N','14.59E'],
        'chile' : ['33.24S','70.40W'],
        'china' : ['39.55N','116.20E'],
        'colombia' : ['04.34N','74.00W'],
        'comros' : ['11.40S','43.16E'],
        'congo' : ['04.09S','15.12E'],
        'costa rica' : ['09.55N','84.02W'],
        "cote d'ivoire" : ['06.49N','05.17W'],
        'croatia' : ['45.50N','15.58E'],
        'cuba' : ['23.08N','82.22W'],
        'cyprus' : ['35.10N','33.25E'],
        'czech republic' : ['50.05N','14.22E'],
        'democratic republic of the congo' : ['04.20S','15.15E'],
        'denmark' : ['55.41N','12.34E'],
        'djibouti' : ['11.08N','42.20E'],
        'dominica' : ['15.20N','61.24W'],
        'dominica republic' : ['18.30N','69.59W'],
        'east timor' : ['08.29S','125.34E'],
        'ecuador' : ['00.15S','78.35W'],
        'egypt' : ['30.01N','31.14E'],
        'el salvador' : ['13.40N','89.10W'],
        'equatorial guinea' : ['03.45N','08.50E'],
        'eritrea' : ['15.19N','38.55E'],
        'estonia' : ['59.22N','24.48E'],
        'ethiopia' : ['09.02N','38.42E'],
        'faroe islands' : ['62.05N','06.56W'],
        'fiji' : ['18.06S','178.30E'],
        'finland' : ['60.15N','25.03E'],
        'france' : ['48.50N','02.20E'],
        'french guiana' : ['05.05N','52.18W'],
        'french polynesia' : ['17.32S','149.34W'],
        'gabon' : ['00.25N','09.26E'],
        'gambia' : ['13.28N','16.40W'],
        'georgia' : ['41.43N','44.50E'],
        'germany' : ['52.30N','13.25E'],
        'ghana' : ['05.35N','00.06W'],
        'greece' : ['37.58N','23.46E'],
        'greenland' : ['64.10N','51.35W'],
        'guadeloupe' : ['16.00N','61.44W'],
        'guatemala' : ['14.40N','90.22W'],
        'guernsey' : ['49.26N','02.33W'],
        'guinea' : ['09.29N','13.49W'],
        'guinea-bissau' : ['11.45N','15.45W'],
        'guyana' : ['06.50N','58.12W'],
        'haiti' : ['18.40N','72.20W'],
        'honduras' : ['14.05N','87.14W'],
        'hungary' : ['47.29N','19.05E'],
        'iceland' : ['64.10N','21.57W'],
        'india' : ['28.37N','77.13E'],
        'indonesia' : ['06.09S','106.49E'],
        'iran' : ['35.44N','51.30E'],
        'iraq' : ['33.20N','44.30E'],
        'ireland' : ['53.21N','06.15W'],
        'israel' : ['31.71N','35.10W'],
        'italy' : ['41.54N','12.29E'],
        'jamaica' : ['18.00N','76.50W'],
        'jordan' : ['31.57N','35.52E'],
        'kazakhstan' : ['51.10N','71.30E'],
        'kenya' : ['01.17S','36.48E'],
        'kiribati' : ['01.30N','173.00E'],
        'kuwait' : ['29.30N','48.00E'],
        'kyrgyzstan' : ['42.54N','74.46E'],
        'laos' : ['17.58N','102.36E'],
        'latvia' : ['56.53N','24.08E'],
        'lebanon' : ['33.53N','35.31E'],
        'lesotho' : ['29.18S','27.30E'],
        'liberia' : ['06.18N','10.47W'],
        'libya' : ['32.49N','13.07E'],
        'liechtenstein' : ['47.08N','09.31E'],
        'lithuania' : ['54.38N','25.19E'],
        'luxembourg' : ['49.37N','06.09E'],
        'macao, china' : ['22.12N','113.33E'],
        'madagascar' : ['18.55S','47.31E'],
        'macedonia' : ['42.01N','21.26E'],
        'malawi' : ['14.00S','33.48E'],
        'malaysia' : ['03.09N','101.41E'],
        'maldives' : ['04.00N','73.28E'],
        'mali' : ['12.34N','07.55W'],
        'malta' : ['35.54N','14.31E'],
        'martinique' : ['14.36N','61.02W'],
        'mauritania' : ['20.10S','57.30E'],
        'mayotte' : ['12.48S','45.14E'],
        'mexico' : ['19.20N','99.10W'],
        'moldova' : ['47.02N','28.50E'],
        'mozambique' : ['25.58S','32.32E'],
        'myanmar' : ['16.45N','96.20E'],
        'namibia' : ['22.35S','17.04E'],
        'nepal' : ['27.45N','85.20E'],
        'netherlands' : ['52.23N','04.54E'],
        'new caledonia' : ['22.17S','166.30E'],
        'new zealand' : ['41.19S','174.46E'],
        'nicaragua' : ['12.06N','86.20W'],
        'niger' : ['13.27N','02.06E'],
        'nigeria' : ['09.05N','07.32E'],
        'norfolk island' : ['45.20S','168.43E'],
        'north korea' : ['39.09N','125.30E'],
        'norway' : ['59.55N','10.45E'],
        'oman' : ['23.37N','58.36E'],
        'pakistan' : ['33.40N','73.10E'],
        'palau' : [')7.5004N','134.6243E'],
        'panama' : ['09.00N','79.25W'],
        'papua new guinea' : ['09.24S','147.08E'],
        'paraguay' : ['25.10S','57.30W'],
        'peru' : ['12.00S','77.00W'],
        'philippines' : ['14.40N','121.03E'],
        'poland' : ['52.13N','21.00E'],
        'portugal' : ['38.42N','09.10W'],
        'puerto rico' : ['18.28N','66.07W'],
        'qatar' : ['25.15N','51.35E'],
        'republic of korea' : ['37.31N','126.58E'],
        'romania' : ['44.27N','26.10E'],
        'russian federation' : ['55.45N','37.35E'],
        'rawanda' : ['01.59S','30.04E'],
        'saint kitts and nevis' : ['17.17N','62.43W'],
        'saint lucia' : ['14.02N','60.58W'],
        'saint pierre and miquelon' : ['46.46N','56.12W'],
        'saint vincent and the greenadines' : ['13.10N','61.10W'],
        'samoa' : ['13.50S','171.50W'],
        'san marino' : ['43.55N','12.30E'],
        'sao tome and principe' : ['00.10N','06.39E'],
        'saudi arabia' : ['24.41N','46.42E'],
        'senegal' : ['14.34N','17.29W'],
        'sierra leone' : ['08.30N','13.17W'],
        'slovakia' : ['48.10N','17.07E'],
        'slovenia' : ['46.04N','14.33E'],
        'solomon islands' : ['09.27S','159.57E'],
        'somalia' : ['02.02N','45.25E'],
        'south africa' : ['25.44S','28.12E'],
        'spain' : ['40.25N','03.45W'],
        'sudan' : ['15.31N','32.35E'],
        'suriname' : ['05.50N','55.10W'],
        'swaziland' : ['26.18S','31.06E'],
        'sweden' : ['59.20N','18.03E'],
        'switzerland' : ['46.57N','07.28E'],
        'syria' : ['33.30N','36.18E'],
        'tajikistan' : ['38.33N','68.48E'],
        'thailand' : ['13.45N','100.35E'],
        'togo' : ['06.09N','01.20E'],
        'tonga' : ['21.10S','174.00W'],
        'tunisia' : ['36.50N','10.11E'],
        'turkey' : ['39.57N','32.54E'],
        'turkmenistan' : ['38.00N','57.50E'],
        'tuvalu' : ['08.31S','179.13E'],
        'uganda' : ['00.20N','32.30E'],
        'ukraine' : ['50.30N','30.28E'],
        'united arab emirates' : ['24.28N','54.22E'],
        'united kingdom' : ['51.36N','00.05W'],
        'tanzania' : ['06.08S','35.45E'],
        'united states' : ['39.91N','77.02W'],
        'uruguay' : ['34.50S','56.11W'],
        'uzbekistan' : ['41.20N','69.10E'],
        'vanuatu' : ['17.45S','168.18E'],
        'venezuela' : ['10.30N','66.55W'],
        'vietnam' : ['21.05N','105.55E'],
        'serbia' : ['44.50N','20.37E'],
        'zambia' : ['15.28S','28.16E'],
        'zimbabwe' : ['17.43S','31.02']
    }

    def material_footprint(materials):
        # outputted as kilograms of CO2 outputted per 2 square meters of raw material created
        footprint = {
            "cotton" : 8.3,
            "fabric" : 11.53,
            "linen" : 4.5,
            "nylon" : 7.31,
            "silk" : 7.63,
            "wool" : 13.89,
            "polyester" : 6.4,
        }
        
        score = 0
        
        for k, v in materials.items():
            score += footprint[k] * (v / 100)
            
        return round(score / 4, 2)

    def shipping_footprint(country):
        
        country = country.strip().lower()
        
        lat1 = float(countries['canada'][0][:-1]) if countries['canada'][0][-1] == 'N' else float(countries['canada'][0][:-1]) * -1
        lat2 = float(countries[country][0][:-1]) if countries[country][0][-1] == 'N' else float(countries[country][0][:-1]) * -1
        lon1 = float(countries['canada'][1][:-1]) if countries['canada'][1][-1] == 'E' else float(countries['canada'][1][:-1]) * -1
        lon2 = float(countries[country][1][:-1]) if countries[country][1][-1] == 'E' else float(countries[country][1][:-1]) * -1
        
        r = 6371 # km
        p = pi / 180

        a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
        dist = 2 * r * asin(sqrt(a))
        
        return round((dist / 800) * 0.6, 2)

    def water_usage(materials):
        # for one average tshirt (L of water)
        water_usage = {
            'cotton' : 2700,
            'polyester' : 350,
            'silk' : 376,
            'wool' : 18700,
            'fabric' : 200,
            'linen' : 6.4,
            'nylon' : 600
        }
        
        water_used = 0
        
        for k, v in materials.items():
            water_used += water_usage[k] * (v / 100)
            
        return round(water_used, 2)

    def final_score(fp, wtr, bs):
        final = 0
        if bs > 0:
            # there is a brand score
            if wtr <= 500:
                final += 34
            elif wtr > 500 and wtr < 1200:
                final += 20
            elif wtr >= 1201:
                final += 12
            
            if fp <= 5:
                final += 33
            elif fp < 10 and fp > 5:
                final += 20
            elif fp >= 10:
                final += 12
                
            if bs >= 75:
                final += 33
            elif bs < 75 and bs > 62:
                final += 22
            elif bs < 62:
                final += 18
            
        else:
            # no brand score
            if wtr <= 500:
                final += 50
            elif wtr > 500 and wtr < 1200:
                final += 42
            elif wtr >= 1201:
                final += 32
            
            if fp <= 5:
                final += 50
            elif fp < 10 and fp > 5:
                final += 42
            elif fp >= 10:
                final += 32
        return final
    
    footprint = round(material_footprint(makeup) + shipping_footprint(coa), 2)
    water = water_usage(makeup)

    brand_description = ''

    if brand_score > 0:
        brand_description = f"{brand.title()}'s ethical manufacturing practice is rated {brand_score}/100"
        print(brand_description)
    elif brand_score == 0:
        brand_description = f"Your manufacturer is {brand}, however ethicality of {brand} can not be confirmed."
        print(brand_description)
    else:
        brand_description = f"Manufacturer was not able to be detected."
        print(brand_description)
    if brand_score > 0:
        return [material_footprint(makeup), shipping_footprint(coa), water, brand_score, final_score(footprint, water, brand_score), brand_description]
    else:
        return [material_footprint(makeup), shipping_footprint(coa), water, -1, final_score(footprint, water, brand_score), brand_description]