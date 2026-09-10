from numpy import isclose

c = 0.3
d = 0.1 + 0.1 + 0.1

print(f"           c: {c}")
print(f"           d: {d}")
print(f"isclose(c,d): {isclose(c, d)}")
print(f"         c=d: {c == d}")
