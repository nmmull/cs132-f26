from numpy import isclose

# carfully chosen very large number
c = 100000000000000010241

d = c / 7 / 10 * 7
e = c / 10

print(f"             d: {d}")
print(f"             e: {e}")
print(f"  isclose(d,e): {isclose(d, e)}")
print(f"isclose(d-e,0): {isclose(d - e, 0)}")
print(f"           d-e: {d - e}")
