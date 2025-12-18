from Binary import bin_float


for i in range(1, 65):
    print(f"Regular: {bin(i)}, Float: {bin_float(float(i))}")