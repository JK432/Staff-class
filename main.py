# Create a class called Staff with staff_code and staff_name as attributes. Create two sub classes Teacher (subject, publication) Typist(speed) from parent class Staff

class staff():
  def __init__(self,stafcod,stafname):
    self.name=stafname
    self.code=stafcod


class teacher(staff):
  def __init__(self,name,code,sub,pub):
    self.sub=sub
    self.pub=pub
    staff.__init__(self,code,name)

    print("name:",self.name)
    print("code:",self.code)
    print("job:Teacher")
    print("subject:",self.sub)
    print("publication",self.pub)
    


class typist(staff):
  def __init__(self,name,code,speed):
    self.speed=speed
    staff.__init__(self,code,name)
    print("")
    print("name:",self.name)
    print("code:",self.code)
    print("job:Typist")
    print("speed:",self.speed)


s1=teacher("JK",4302,"c","jkpub")
s2=typist("JacK",4302,450)



