
def Config():
    # Open the file in read mode
    with open('app.config', 'r') as f:
        lines = f.readlines()

    # Initialize an empty dictionary
    data = {}

    # Loop through each line in the file
    for line in lines:

        try:
        #if len(line) > 0:
            # Split the line at the equals sign
            key, value = line.strip().split('=')
            # Add the key-value pair to the dictionary
            data[key] = value
        except Exception as e:
            pass

    return data


def ReadConfig(section):
    with open('app.config', 'r') as f:
        config = f.read().split('\n\n')

    print(config)

    config_dict = {}
    try:
        for block in config:
            lines = block.split('\n')
            header = lines[0].strip('[]')
            if header == section:
                for line in lines[1:]:
                    key, value = line.split('=')
                    config_dict[key] = value
    except:
        pass

    return config_dict

# usage
user_dict = ReadConfig('Server')
print(user_dict)



"""
file: app.config

[User]
name=dave
city=SA California
Country=USA 

[Server]
host=127.0.0.1
port=8080
path=/v1/fileinfo
name=dave
city=SA California
Country=USA 
into dictionary
or something else

"""
