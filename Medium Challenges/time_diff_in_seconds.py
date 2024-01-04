from datetime import datetime, timedelta

def time_difference(t1, t2):
    format_str = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.strptime(t1, format_str)
    time2 = datetime.strptime(t2, format_str)
    return int(abs((time1 - time2).total_seconds()))
def main():
    n = int(input())
    for _ in range(n):
        t1 = input().strip()
        t2 = input().strip()
        result = time_difference(t1, t2)
        print(result)
if __name__ == "__main__":
    main()
