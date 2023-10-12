def linearSearchProduct(productlist, targetproduct):
  indices = []
  for index, product in enumerate(productlist):
    if product == targetproduct:
      indices.append(index)
  return indices
products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = 'apple'
print("SEARCH ELEMENT FOUND AT THE POSITION")
print("~~~~~~~~~~~~")
result = linearSearchProduct(products, target)
print("SEARCH 1:", target, result)
result = linearSearchProduct(products, target2)
print("SEARCH 2:", target2, result)