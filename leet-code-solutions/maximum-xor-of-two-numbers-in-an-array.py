class Solution:
  def findMaximumXOR(self, nums: List[int]) -> int:
			self.root = {}
			max_val = 0
			self.insert(nums[0])
			for n in nums:
				max_val = max(self.max_xor_helper(n),max_val)
				self.insert(n)

			return max_val
        
  def insert(self, n) :
        temp = self.root
        i = 31
        while i >= 0 :
            bit = (n >> i) & 1
            if bit not in temp:
                temp[bit] = {}
            temp = temp[bit]
            i -= 1
        
    
  def max_xor_helper(self, value) :
			temp = self.root
			current_ans = 0
			i = 31
			while i >= 0:
				bit = (value >> i) & 1
				if bit^1 in  temp:
					temp = temp[bit^1]
					current_ans += (1 << i)

				elif bit in  temp:
					temp = temp[bit]
					
				else:
					return current_ans
				i -= 1
			return current_ans