class ExtendedStack(list):

    def sum(self):
        if len(self) >= 2:
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1 + top2)
    def sub(self):
        if len(self) >= 2:
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1 - top2)
    def mul(self):
        if len(self) >= 2:
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1 * top2)
    def div(self):
        if len(self) >= 2:
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1 // top2)