from internet import InternetService

def main():
    # Exercise 1
    arr: list[int] = [1, 2, 3, 4, 5, 2]
    arr2: list[int] = [5, 6, 7, 8, 9, 2]
    # lambda analog on python
    lambda_func = lambda value1, value2: [bool(x == y) for x, y in zip(value1, value2)]
    # anonymous method analog on python
    def anonymous_func(value1: list[int], value2: list[int]) -> list[bool]:
        return [bool(x == y) for x, y in zip(value1, value2)]
    
    anonymous_method = anonymous_func
    print(anonymous_method(arr, arr2))
    print(lambda_func(arr, arr2))
    # Exercise 2
    service = InternetService(traffic_limit=3.0)
    
    # sends a lambda as an event handler to a list
    service.traffic_exceeded += lambda sender, args: print(f"Traffic exceeded: {args.traffic_amount} GB")
    service.use_internet(5)
    service.use_internet(7)


if __name__ == "__main__":
    main()