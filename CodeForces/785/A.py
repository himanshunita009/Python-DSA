def main():
    n = int(input())
    mp = dict()
    mp["Tetrahedron"] = 4 
    mp["Cube"] = 6 
    mp["Octahedron"] = 8 
    mp["Dodecahedron"] = 12 
    mp["Icosahedron"] = 20 
    ans = 0
    for _ in range(n):
        shape = input()
        ans += mp[shape]
    print(ans)

main()