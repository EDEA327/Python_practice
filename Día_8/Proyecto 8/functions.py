def cosmetics_generator() -> str:
    for shift in range(1,10000):
        yield f"C-{shift}"


def pharmacy_generator() -> str:
    for shift in range(1,10000):
        yield f"P-{shift}"


def perfumery_generator() -> str:
    for shift in range(1,10000):
        yield f"Pe-{shift}"


cg = cosmetics_generator()
pg = pharmacy_generator()
peg = perfumery_generator()


def decorator(category):
    print("\n" + "*" * 30)
    print("Your shift is: ")

    if category == "C":
        print(next(cg))
    elif category == "P":
        print(next(pg))
    else:
        print(next(peg))
    print("Please wait...")

