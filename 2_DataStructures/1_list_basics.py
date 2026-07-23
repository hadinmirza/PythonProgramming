colors = ["red", "green", "blue"]  # List Created 
colors.append("yellow")   # append function used to add at the end of lists
colors.insert(0, "black") # insert function can add at at index i.e first parameter is index and seconf is value to be inserted 

# Display the whole list
print("Colors:", colors)

totalColors = len(colors)
print (f"Total Number of Colors are : {totalColors}") # Display the total number of colors

# Display the last color
print("Last color:", colors[-1]) 