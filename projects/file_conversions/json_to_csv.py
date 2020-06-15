import json
import csv


def create_json_data(output_file):
    customer = {}
    customer['11111'] = {
        'cust_id': 11111,
        'cust_name': 'Stylish Gal',
        'item_id': 873303,
        'item_price': 35,
        'token': 'c59faf336a20d9bb49305a8017defe55c04c13429f0ce42ef171be34c3c48c39'
        }
    customer['11112'] = {
        'cust_id': 11112,
        'cust_name': 'Stylish Gent',
        'item_id': 873303,
        'item_price': 65,
        'token': 'f0a96be49780acb4ffabbc5902a443d0ba02e90c4ae54cf7ac2ca9762190bbe2'
        }
    
    dumping_data_to_json = json.dumps(customer)
    with open(output_file, 'w') as f:
        f.write(dumping_data_to_json)

    return output_file

    
def convert_json_to_csv(json_file,csv_file):
    with open(json_file,'r') as j, open(csv_file,'w') as c: 
        writeable_file = csv.writer(c)
        readable_file = json.loads(j.read())        
        
        writeable_file.writerow(['cust_id', 'cust_name', 'item_id', 'item_price', 'token'])

        for id in readable_file:
            writeable_file.writerow([readable_file[id]['cust_id'],
                             readable_file[id]['cust_name'],
                             readable_file[id]['item_id'],
                             readable_file[id]['item_price'],
                             readable_file[id]['token']])        
            
            
    return csv_file

customer_data_json = create_json_data('customer_data.json')
customer_data_csv = convert_json_to_csv(customer_data_json,'customer_data.csv')
#

#