class Solution:
    def addBinary(self, a: str, b: str) -> str:

        result = []
        carry = 0

        i = len(a) -1
        j = len(b) - 1

        while i >=0 or j >=0 or carry > 0:
            digitA = int(a[i]) if i >=0 else 0
            digitB = int(b[j]) if j >=0 else 0

            total = (digitA + digitB + carry)
            result.append(str(total%2)) #% 2 # converts to binary and then convert to string as we need concat for the result 
            carry = total // 2

            i -=1
            j -=1

        result.reverse()

        return "".join(result)



        