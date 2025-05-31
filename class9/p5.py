#multilevel inheritence


class A:
  def __init__(self,a1):
    self.a1 = a1
  def aa(self):
    return self.a1

class B(A):
  def bb(self):
    return self.a1

class C(B):
  def cc(self):
    return self.a1

c = C(14)
b = B(13)
print(c.bb(),b.aa(),c.aa())
