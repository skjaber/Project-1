#single inheritence


class A:
  def __init__(self,a1):
    self.a1 = a1
  def aa(self):
    return self.a1

class B(A):
  def bb(self):
    return self.a1

b = B(10)
print(b.aa())
