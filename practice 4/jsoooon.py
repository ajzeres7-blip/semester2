import json
with open('sample-data.json', 'r') as file:
    data=json.load(file)

#Heading printer
print("Interface Status")
print("="*80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print('-'*50 + ' '+'-'*20 + ' '+'-'*7+' '+'-'*6)

#Rows
for item in data.get('imdata', []):
    attributes = item.get('l1PhysIf', {}).get('attributes', {})

    dn = attributes.get('dn', '')
    descr=attributes.get('descr','')
    speed=attributes.get('speed','')
    mtu=attributes.get('mtu','')

    print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")
    