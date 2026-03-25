with open("input2.txt", "r") as file:
    total_paper = 0
    total_ribbon = 0
    for line in file:
        whl = [int(x) for x in line.strip().split('x')]
        whl.sort()
        package_paper = 2*whl[0]*whl[1] + 2*whl[1]*whl[2] + 2*whl[2]*whl[0] + whl[0]*whl[1]
        total_paper += package_paper
        total_ribbon += whl[0]*whl[1]*whl[2] + 2*whl[0]+2*whl[1]

print("Total paper in sqr feet", total_paper)
print("Total ribbon in feet", total_ribbon)
