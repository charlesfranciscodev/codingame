def print_tree(tree)
  output = ""
  if (!tree.empty?)
    i = 0
    while (i < tree.size - 1)
      output += tree[i] + " > "
      i += 1
    end
    output += tree[i]
    puts(output)
  end
end

nb_people = gets.to_i
tree = [] # partial family tree

nb_people.times {
  line = gets.strip
  name = line.tr(".", "").chomp
  name_level = line.size - name.size
  tree_level = tree.size
  if (name_level == 0)
    if (!tree.empty?)
      print_tree(tree)
      tree.clear()
    end
  elsif (name_level < tree_level)
    print_tree(tree)
    while (name_level < tree.size)
      tree.pop()
    end
  end
  tree.push(name)
}
print_tree(tree)
