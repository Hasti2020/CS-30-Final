from tabulate import tabulate

# Sample 2D list (table data)
table_data = [
    ["Name", "House", "Year"],
    ["Harry", "Gryffindor", 1],
    ["Hermione", "Gryffindor", 1],
    ["Draco", "Slytherin", 1]
]

# Print the table using tabulate
print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
