class Math:
    def add(self, a, b, c=0):  # Default argument for c
        return a + b + c

m = Math()
print(m.add(2, 3))      # Output: 5  (calls add(a, b))
print(m.add(2, 3, 4))   # Output: 9  (calls add(a, b, c))
