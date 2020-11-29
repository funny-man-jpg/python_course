import math

def circumference(r):
  """Calculates the circumference given the radius
  
  Parameters
  ----------
  r : float
    The radius in m
  
  Returns
  -------
  float
    the circumference 2*pi*r
  """
  return 2*math.pi*r
def area(r):
  """Calculates the area given the radius
  
  Parameters
  ----------
  r : float
    The radius in m
  
  Returns
  -------
  float
    the area in m^2
  """
  return math.pi*r**2

