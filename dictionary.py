   1  def most_frequent(string):
   2      d = dict()
   3      for key in string:
   4          if key not in d:
   5              d[key] = 1
   6          else:
   7              d[key] += 1
   8      return d
   9  print most_frequent('aabbbc')
  10      {'a': 2, 'c': 1, 'b': 3}
  
           
