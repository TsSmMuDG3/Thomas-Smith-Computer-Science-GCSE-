x = input()
str(x)

def sum_year_digits(year):
  return sum(int(digit) for digit in str(year))
year = input()
result = sum_year_digits(year)
print("The sum of the digits of ",year," is:",result)

tile_cost = float(input("How much does each tile cost"))
tile_width = float(input("How wide is each tile"))
tile_length = float(input("How long is each tile"))
floor_width = float(input("How wide is the floor"))
floor_length = float(input("How long is the floor"))
tile_area = tile_width * tile_length
floor_area = floor_width * floor_length
import math
tiles_needed = math.ceil(floor_area / tile_area)
total_cost = tiles_needed * tile_cost
print(total_cost)

text = input("Enter a sentence: ")
reversed_text = text[:-1]
print(reversed_text)
