from typing import List

def encode(strs: List[str]) -> str:
    encoded = ""
    for s in strs:
        encoded += str(len(s)) + ":" + s
    return encoded

def decode(s: str) -> List[str]:
    result = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != ":":
            j += 1
        length = int(s[i:j])
        result.append(s[j+1:j+1+length])
        i = j + 1 + length
    return result

print(encode(["Hello", "world"]))
print(decode(encode(["Hello", "world"])))

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you handle strings that contain the delimiter character ':' in your encoding scheme?
2. What if you need to encode and decode nested lists or more complex data structures?

=== REAL WORLD APPLICATION ===
Network Protocol Design: Used in communication systems to serialize and transmit string arrays over network connections, ensuring reliable data transmission between client-server applications and microservices.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(n) for both encode and decode
- Encode: O(n) where n = total length of all strings
- Decode: O(n) where n = length of encoded string
- Each character is processed exactly once

Space Complexity: O(n)
- Encode: O(n) for the encoded string
- Decode: O(n) for the result list and intermediate processing
- Linear in the size of input/output data
'''