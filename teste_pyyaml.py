import yaml
import json

data2 = [
    {
    'apiVersion': 'v1',
    'kind':'persistentVolume',
    'metadata': {'name':'mongodb-pv', 'labels':{'type':'local'}},
    'spec':{'storageClassName':'hostpath'},
    'capacity':{'storage':'3Gi'},
    'accessModes':['ReadWriteOnce'],
    'hostpath':{'path':'/mnt/data'}
    },

    {
    'apiVersion': 'v1',
    'kind':'persistentVolume',
    'metadata': {'name':'mysql-pv', 'labels':{'type':'local'}},
    'spec':{'storageClassName':'hostpath'},
    'capacity':{'storage':'2Gi'},
    'accessModes':['ReadWriteOnce'],
    'hostpath':{'path':'/mnt/data'}
    }
]

yaml_output2 = yaml.dump_all(data2, sort_keys=False)
print(yaml_output2)

def write_yaml_to_file(py_obj,filename):
    with open(f'{filename}.yaml', 'w',) as f :
        yaml.dump_all(py_obj,f,sort_keys=False) 
    print('Written to file successfully')

write_yaml_to_file(data2, 'teste_pyyaml')

print ('------------------------------------------------------------')

def read_multiple_block_of_yaml_data(filename):
    with open(f'{filename}.yaml','r') as f:
        data = yaml.safe_load_all(f)
        print(list(data)) 

read_multiple_block_of_yaml_data('teste_pyyaml')

print ('------------------------------------------------------------')

def read_modify_save_yaml_data(filename,index,key,value,write_file):
    with open(f'{filename}.yaml','r') as f:
        data = yaml.safe_load_all(f)
        loaded_data = list(data)
        loaded_data[index][f'capacity'][f'storage'] = 'none'
        loaded_data[index][f'{key}'].append(f'{value}')
    with open(f'{write_file}.yaml', 'w') as file:
        yaml.dump_all(loaded_data,file, sort_keys=False)
    print(loaded_data) 
    
read_modify_save_yaml_data('teste_pyyaml', 0, 'accessModes', \
'ReadOnlyMany', 'teste_pyyaml_modified')

print ('------------------------------------------------------------')

def convert_yaml_to_json(yfile, jfile):
    with open(f'{yfile}.yaml', 'r') as f:
        yaml_file = yaml.safe_load_all(f)
        loaded_data = list(yaml_file)
    with open(f'{jfile}.json', 'w') as json_file:
        json.dump(loaded_data, json_file, indent=3)
    print('done!')
convert_yaml_to_json('teste_pyyaml_modified','teste_pyyaml_modified')
