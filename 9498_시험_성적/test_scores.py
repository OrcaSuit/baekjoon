import sys

def get_grade(score):
    if score < 60:
        return "F"
    elif score < 70:
        return "D"
    elif score < 80:
        return "C"
    elif score < 90:
        return "B"
    else:
        return "A"

def main():
    score = int(sys.stdin.readline())
    print(get_grade(score))

if __name__ == "__main__":
    main()
