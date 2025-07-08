import json

# Loading JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Targetting module_id to be deleted
target_module_id = "portfolioVolatility"
deletion_done = False

# Recursive function to remove the dict with the target module_id
def remove_module_by_id(node, module_id):
    global deletion_done
    if deletion_done:
        return
    
    if isinstance(node, list):
        for i in range(len(node) -1, -1, -1):  # Iterating backwards to delete safely
            item = node[i]
            if isinstance(item, dict) and item.get('module_id') == module_id:
                del node[i]
                deletion_done = True
                return
            else:
                remove_module_by_id(item, module_id)
    elif isinstance(node, dict):
        for key in node:
            remove_module_by_id(node[key], module_id)


# Performing the deletion
remove_module_by_id(data, target_module_id)

# Output to a new JSON file
with open('data_cleaned.json', 'w') as file:
    json.dump(data, file, indent= 2)


print(f'Deleted module with module_id: {target_module_id}')