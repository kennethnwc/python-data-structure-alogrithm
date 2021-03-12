class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        def condition(value):
            
            need = 1
            remain = value
            
            for i in range(len(weights)):
                if remain >= weights[i]:
                    remain -= weights[i]
                else:
                    need += 1
                    remain = value - weights[i]
                    
            return need <= D
                
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
    
