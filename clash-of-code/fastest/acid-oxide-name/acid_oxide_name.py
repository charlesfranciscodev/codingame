def acid_oxide_name(nonmetalNum: int, nonmetal: str, oxideNum: int):
    nonmetal_prefixes = ["", "mon", "di", "tri", "tetra", "penta"]
    oxide_prefixes = ["", "mon", "di", "tri", "tetr", "pent"]

    nonmetal_prefix = nonmetal_prefixes[nonmetalNum] if nonmetalNum != 1 else ""
    oxide_prefix = oxide_prefixes[oxideNum] if oxideNum != 1 else "mon"

    return nonmetal_prefix + nonmetal + " " + oxide_prefix + "oxide"


if __name__ == "__main__":
    # Taking input
    nonmetalNum, nonmetal = input().split()
    oxideNum = int(input())

    # Calling the function and printing the output
    print(acid_oxide_name(int(nonmetalNum), nonmetal, oxideNum))
