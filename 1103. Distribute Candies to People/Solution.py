class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        output = []
            
        for num in range(num_people):
            output.append(0)
        i = 1
        while (candies > 0):
           
            for person in range(num_people):
                give = 0
                
                if i <= candies:
                    candies -= i;
                    give = i
                    i += 1
                elif i == candies:
                    give = i
                    candies = 0
                else:
                    give = candies
                    candies = 0
                    
                output[person] += give
        
        return output        