import json
person = {
    'firstname':'Anitha',
    'Lastname':'Sarangan',
    'age':42,
    'address':{"streeraddress":"22 301 Palisades way",
               "Zip":"t8h0t4"
               }

    }
with open('person.json','w') as f:
    json.dump(person,f)

# Serializing json  
json_object = json.dumps(person, indent = 4) 
  
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 

#print(json_object)

# Opening JSON file 
with open('sample.json', 'r') as openfile: 
  
    # Reading from json file 
    json_object = json.load(openfile) 
  
print(json_object) 
print(type(json_object)) 
