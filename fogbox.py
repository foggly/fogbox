class File(object):
    def __init__ (self):
        self.current = 0
        self.file = 0
        self.red=""
    def openenc(self, location):
      self.file=open(location,'r')
      for i in self.file:
        self.red=self.file.read()
      return 1
    def opendec(self,location):
      write(self.file)
        return self.current

infile = open(fname, 'r')
data = infile.read()
print(data)
