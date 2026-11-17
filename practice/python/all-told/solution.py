def sum_list(counts: list) -> int:
  var=0
  for i in range(len(counts)):
    var = var + counts[i]
    if i == len(counts):
      break
  return var
