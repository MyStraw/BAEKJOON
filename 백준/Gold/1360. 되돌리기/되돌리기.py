def isAlpha(x):
    return int(x) if x.isdigit() else x
class Return:
    def __init__(self, orders, types, sec): 
        self.orders = orders
        self.types = isAlpha(types)
        self.sec = sec
        self.alive = True
    def get_orders(self):
        return self.orders
    def get_types(self):
        return self.types
    def get_sec(self):
        return self.sec    
    def imAlive(self):
        return self.alive
    def kill(self):
        self.alive = False   
    def toString(self):
        return f"Return({self.orders}, {self.types}, {self.sec}, alive = {self.alive})"
    
N = int(input())
dqq = []
result = []
for i in range(N):
    line = input().split()
    orders = line[0]
    types = line[1]
    sec = int(line[2])    
    cmd = Return(orders, types, sec)
    dqq.append(cmd)
for i in range(len(dqq)-1, -1, -1):
    cur_cmd = dqq[i]
    if not cur_cmd.imAlive():
        continue
    if cur_cmd.get_orders() == "undo":
        t = cur_cmd.get_types()
        now = cur_cmd.get_sec()
        for j in range(i-1, -1, -1):
            target_cmd = dqq[j]
            if target_cmd.imAlive() and now - t <= target_cmd.get_sec() < now:
                target_cmd.kill()
    
for cmd in dqq:
    if cmd.imAlive() and cmd.get_orders() == "type":
        result.append(cmd.get_types())           
print("".join(result))        