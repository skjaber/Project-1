#multiple inheritance

class A:
  def __init__(self,a1):
    self.a1 = a1
  def aa(self):
    return self.a1

class B:
  def __init__(self,b1):
    self.b1 = b1
  def bb(self):
     return self.b1

class C(A,B):
  def __init__(self,a1,b1):
    A.__init__(self,a1)
    B.__init__(self,b1)
  def cc(self):
    return self.a1,self.b1

c = C(A,B)
print(c.aa(),c.bb())

