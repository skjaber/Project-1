#hybrid inheritance

class A:
  def __init__(self,a1):
    self.a1 = a1
  def aa(self):
    return self.a1

class B(A):
  def bb(self):
    return self.a1

class C(A):
  def cc(self):
    return self.a1

class D(B):
  def dd(self):
    return self.a1


b = B(10)
c = C(20)
d = D(30)
print(b.aa(),c.aa(),d.aa(),d.bb())
