class Counter:
    def __init__(self):
        self.count = 0

    def push(self):
        self.count +=1
        return self.count

    def reset(self):
        self.count = 0
        return self.count



def main():
    mycount = Counter()
    print(mycount.push())
    print(mycount.push())
    print(mycount.reset())
    print(mycount.push())


if __name__ == "__main__":
    main()