import re


VALUE_TYPE = "VALUE"
REFERENCE_TYPE = "REFERENCE"
EMPTY_TYPE = "EMPTY"

VALUE_PATTERN = re.compile(r"^-?[0-9]+$")
REFERENCE_PATTERN = re.compile(r"^\$[0-9]+$")


def get_arg_type(arg):
    if VALUE_PATTERN.search(arg):
        return VALUE_TYPE
    if REFERENCE_PATTERN.search(arg):
        return REFERENCE_TYPE
    return EMPTY_TYPE


def value(arg_type, arg, formulas, values):
    if arg_type == REFERENCE_TYPE:
        index = int(arg[1:])
        if index not in values:
            parse_formula(index, formulas, values)
        return values[index]
    return int(arg)


def parse_formula(i, formulas, values):
    formula = formulas[i]
    operation, arg1, arg2 = formula.split()
    arg_type1 = get_arg_type(arg1)
    arg_type2 = get_arg_type(arg2)

    if operation == "VALUE":
        values[i] = value(arg_type1, arg1, formulas, values)
    else:
        value1 = value(arg_type1, arg1, formulas, values)
        value2 = value(arg_type2, arg2, formulas, values)
        if operation == "ADD":
            values[i] = value1 + value2
        elif operation == "SUB":
            values[i] = value1 - value2
        else:
            values[i] = value1 * value2


if __name__ == "__main__":
    formulas = []
    values = {}

    # read input formulas
    nb_cells = int(input())
    for _ in range(nb_cells):
        formulas.append(input())

    # parse formulas
    for i in range(nb_cells):
        parse_formula(i, formulas, values)

    # output values
    for i in range(nb_cells):
        print(values[i])
