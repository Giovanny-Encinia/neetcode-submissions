class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        if not operations:
            return 0

        for op in operations:
            
            if op.lstrip("-").isdigit():
                record.append(int(op))
            elif op == "+":
                second = record[-1]
                first = record[-2]
                record.append(first + second)
            elif op == "D":
                record.append(record[-1] * 2)
            elif op == "C":
                record.pop()
        
        return sum(record)

                
                    