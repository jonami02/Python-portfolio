import collections

x = collections.deque(["Mon","Tue","wed"])
print(x)

print("Append to right")
x.append("Thu")
print(x,"\n")

print("Append to left")
x.appendleft("Sun")
print(x,"\n")

print("Removing from the right")
x.pop()
print(x,"\n")

print("Removing from the left")
x.popleft()
print(x,"\n")
