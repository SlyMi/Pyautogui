import sys
import time


def main() -> str:
    time_str = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    print(time_str)


if __name__ == "__main__":
    main()
