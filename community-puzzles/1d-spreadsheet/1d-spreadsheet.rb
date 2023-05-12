VALUE_TYPE = "VALUE"
REFERENCE_TYPE = "REFERENCE"
EMPTY_TYPE = "EMPTY"

VALUE_PATTERN = /^-?[0-9]+$/
REFERENCE_PATTERN = /^\$[0-9]+$/

def get_arg_type(arg)
  return VALUE_TYPE if VALUE_PATTERN.match(arg)
  return REFERENCE_TYPE if REFERENCE_PATTERN.match(arg)

  return EMPTY_TYPE
end

def value(arg_type, arg, formulas, values)
  if arg_type == REFERENCE_TYPE
    index = arg[1..-1].to_i
    parse_formula(index, formulas, values) unless values.key?(index)
    return values[index]
  end
  return arg.to_i
end

def parse_formula(i, formulas, values)
  formula = formulas[i]
  operation, arg1, arg2 = formula.split
  arg_type1 = get_arg_type(arg1)
  arg_type2 = get_arg_type(arg2)

  if operation == "VALUE"
    values[i] = value(arg_type1, arg1, formulas, values)
  else
    value1 = value(arg_type1, arg1, formulas, values)
    value2 = value(arg_type2, arg2, formulas, values)
    if operation == "ADD"
      values[i] = value1 + value2
    elsif operation == "SUB"
      values[i] = value1 - value2
    else
      values[i] = value1 * value2
    end
  end
end

formulas = []
values = {}

# read input formulas
nb_cells = gets.to_i
nb_cells.times do
  formulas << gets.chomp
end

# parse formulas
nb_cells.times do |i|
  parse_formula(i, formulas, values)
end

# output values
nb_cells.times do |i|
  puts values[i]
end
