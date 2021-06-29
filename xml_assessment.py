#Handle requests
import requests
#turn the xml structure into a series of nested dictionaries
import xmltodict

def url_to_list(url,city=None,state=None):
    response = requests.get(url)
    data = xmltodict.parse(response.content)
    data = data['PhysicalProperty']
    properties = list()
    #Get the list of XML properties
    properties_xml = data['Property']
    for p in properties_xml:
        #Get the address info of a property
        addr = p['PropertyID']['Address']
        #Check if a property is in Madison and is in WI
        if city == None and state ==None:
            property_info = dict()
            try:
                #If a floorplan exists, count the number of bedrooms
                floorplan = p['Floorplan'][0]
                count = 0
                for r in floorplan['Room']:
                    if r['@RoomType']=='Bedroom':
                        count+=float(r['Count'])
            except:
                #If no floorplan exists. Say that a property has 0 bedrooms 
                count = 0
            property_info['property_id'] = p['PropertyID']['Identification']['@IDValue']
            property_info['name'] = p['PropertyID']['MarketingName']
            property_info['email'] = p['PropertyID']['Email']
            property_info['bedrooms'] = str(count)
            #appent the dictionary obj to a list of properties
            properties.append(property_info)
        elif addr['City']==city and addr['State']==state:
            property_info = dict()
            try:
                #If a floorplan exists, count the number of bedrooms
                floorplan = p['Floorplan'][0]
                count = 0
                for r in floorplan['Room']:
                    if r['@RoomType']=='Bedroom':
                        count+=float(r['Count'])
            except:
                #If no floorplan exists. Say that a property has 0 bedrooms 
                count = 0
            property_info['property_id'] = p['PropertyID']['Identification']['@IDValue']
            property_info['name'] = p['PropertyID']['MarketingName']
            property_info['email'] = p['PropertyID']['Email']
            property_info['bedrooms'] = str(count)
            #appent the dictionary obj to a list of properties
            properties.append(property_info)
    return properties