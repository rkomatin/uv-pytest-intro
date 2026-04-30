def is_even(n: int) -> bool:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"is_even() requires an int argument, got {type(n).__name__!r}")
    return n % 2 == 0


def main():
    print("Hello from uv-pytest-intro!")


if __name__ == "__main__":
    main()
