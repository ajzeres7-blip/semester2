import re
import json
def parse_receipt(raw_file_path):
    with open(raw_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    #Find Data and Time
    date_time_match=re.search(r'(\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}\:\d{2})', content)
    date_time = date_time_match.group(1) if date_time_match else 'Not found'
    # Find Payment Method
    payment_match=re.search(r'Банковская карта', content)
    payment_method=payment_match.group(0) if payment_match else 'Unknown'
    # Find Total Amount
    total_match=re.search(r'ИТОГО:\s*([\d\s,.]+)', content)
    total_amount=total_match.group(1).strip() if total_match else '0.00'
    #Find products and prices
    products=[]
    product_pattern=re.compile(r'(\d+)\.\n(.*?)\n[\d,.\s]+x\s+([\d\s,.]+)\n([\d\s,.]+)', re.MULTILINE)
    matches=product_pattern.findall(content)
    for match in matches:
        index, name, unit_price, subtotal=match
        products.append({
            'id': index,
            'name': name.replace('\n', ' ').strip(),
            'unit_price': unit_price.strip(),
            'subtotal': subtotal.strip()
        })

    #Output structured for JSON
    receipt_data={
        'metadata':{
            'date_time': date_time,
            'payment_method': payment_method,
            'total':total_amount           
        },
        'products': products
    }
    return receipt_data
    
if __name__=='__main__':
    data=parse_receipt('raw.txt')
    print('--- RECEIPT SUMMARY ---')
    print(f'Date: {data["metadata"]["date_time"]}')
    print(f'Payment: {data["metadata"]["payment_method"]}')
    print("-"*30)
    for product in data['products']:
        print(f'{product["id"]}.{product["name"][:40]}... | Price: {product["subtotal"]}')
    print("-"*30)
    print(f'TOTAL: {data["metadata"]["total"]}')

    with open('output.json', 'w', encoding='utf-8')as jf:
        json.dump(data, jf, ensure_ascii=False, indent=4)