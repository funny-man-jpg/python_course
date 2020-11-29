def perimeter(a,b,c,d):
  """Calculates the perimeter given the first base, second base, and 2 sides
  
  Parameters
  ----------
  a : float
    The first base in m

  b : float
    The second base in m

  c
    The first side in m

  d
    The second side in m

  Returns
  -------
  float
    the perimeter in a+b+c+d
  """
  return a+b+c+d
def area(t,b,h):
  """Calculates the area given the smaller base, larger base and height
  
  Parameters
  ----------
  t : float
    The smaller base in m

  b
    The larger base in m

  h : float
    The height in m

  Returns
  -------
  float
    the area in (t*b)/2*h
  """
  return (t*b)/2*h