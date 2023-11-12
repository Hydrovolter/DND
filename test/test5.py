import time

for _ in range(4):
    time.sleep(1)
    print("\r{}.".format("." * min(_, 2)), end="")

print("\n\n", end="")
