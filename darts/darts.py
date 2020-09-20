class Rings:
  Inner = 1**2
  Middle = 5**2
  Outer = 10**2


class Points:
  Inner = 10
  Middle = 5
  Outer = 1
  Miss = 0


def score(x, y):
    hit = x**2 + y**2
    if hit <= Rings.Inner: return Points.Inner
    if hit <= Rings.Middle: return Points.Middle
    if hit <= Rings.Outer: return Points.Outer
    return Points.Miss
