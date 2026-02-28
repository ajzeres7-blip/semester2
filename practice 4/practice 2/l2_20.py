import sys
def main():
    input = sys.stdin.readline
    n = int(input())
    document = {}
    for _ in range(n):
        parts = input().strip().split()
        
        if parts[0] == "set":
            _, key, value = parts
            document[key] = value
        
        elif parts[0] == "get":
            _, key = parts
            if key in document:
                print(document[key])
            else:
                print(f"KE: no key {key} found in the document")

if __name__ == "__main__":
    main()
