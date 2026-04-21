def print_attributes(obj):
    for attribute in dir(obj):
        # Skip special attributes
        if not attribute.startswith('__'):
            value = getattr(obj, attribute)
            print(f"{attribute}: {value}")

# Example usage
class Example:
    def __init__(self):
        self.name = "example"
        self.value = 42

example = Example()
print_attributes(example)