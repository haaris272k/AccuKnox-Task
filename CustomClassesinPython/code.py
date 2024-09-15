class Rectangle:
    def __init__(self, **attributes):
        # Store all the passed attributes in a dictionary
        self.attributes = attributes

    def __iter__(self):
        # Iterate over the dictionary and yield each key-value pair as a dict
        for key, value in self.attributes.items():
            yield {key: value}

# Example usage
rect = Rectangle(length=10, width=5, color="blue")

# Iterate over the instance
for attribute in rect:
    print(attribute)
