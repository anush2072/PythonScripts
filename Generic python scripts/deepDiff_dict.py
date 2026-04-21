# pip install deepdiff

a = {'Name': 'Test', 'Age': 5}
b = {'Name': 'Testing', 'Age': 78}

from deepdiff import DeepDiff
diff = DeepDiff(a, b)
print(diff)
