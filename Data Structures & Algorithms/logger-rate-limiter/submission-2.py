class Logger:

    def __init__(self):
        
        self.next_allowed = {} # msg: earliest allowed time

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        next_allowed_time = self.next_allowed.get(message)

        if next_allowed_time is None or timestamp >= next_allowed_time:
            self.next_allowed[message] = timestamp + 10
            return True
        
        return False


        


# Your Logger object will be instantiated and called as such:
obj = Logger()
param_1 = obj.shouldPrintMessage(10,"message")
