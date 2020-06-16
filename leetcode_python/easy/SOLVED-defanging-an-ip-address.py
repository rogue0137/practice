# 1108. Defanging an IP Address
# https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        address_list = list(address)
        for i in range(len(address_list)):
            if address_list[i] == '.':
                address_list[i] = '[.]'
        updated_address = ''.join(address_list)
        return updated_address

# Runtime: 20 ms, faster than 98.49% of Python3 online submissions for Defanging an IP Address.
# Memory Usage: 13.7 MB, less than 78.01% of Python3 online submissions for Defanging an IP Address.