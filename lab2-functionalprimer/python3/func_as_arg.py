def list_func(a, b):
    return list(range(a, b + 1)) 

def applicator_func(inp_func, a, b, s):
    nums = inp_func(a, b)
    if s == 's':
        return sum(nums) 
    else:
        return sum(nums) / len(nums)  

def main():
    a = int(input("Enter start of range: "))
    b = int(input("Enter end of range: "))
    s = input("Enter 's' for sum or anything else for average: ").strip()

    result = applicator_func(list_func, a, b, s)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
