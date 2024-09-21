import pandas as pd

class AttributeTable:
    def __init__(self):
        self.data = pd.DataFrame(columns=['Node', 'Attribute'])

    def add_node_attribute(self, node, attribute):
        # Create a DataFrame from the new attribute and concatenate
        new_entry = pd.DataFrame({'Node': [node], 'Attribute': [attribute]})
        self.data = pd.concat([self.data, new_entry], ignore_index=True)

    def remove_node_attribute(self, node):
        self.data = self.data[self.data['Node'] != node]

    def get_attributes(self, node):
        row = self.data[self.data['Node'] == node]
        return row['Attribute'].values[0] if not row.empty else "No attributes"

    def __str__(self):
        return str(self.data)


#Example Usage
def main():
    # Using Attribute Table
    attribute_table = AttributeTable()
    attribute_table.add_node_attribute('A', {'age': 25, 'location': 'NY'})
    print("Attribute Table:", attribute_table)

if __name__ == "__main__":
    main()