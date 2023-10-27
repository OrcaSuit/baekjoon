def is_leap_year(year):
    if year % 400 == 0:
        return 1
    if year % 100 == 0:
        return 0
    if year % 4 == 0:
        return 1
    return 0

def main():
    year = int(input())
    print(is_leap_year(year))

if __name__ =="__main__":
    main()