def checkInvalidSegment(segment):
    return (
        segment == '' or
        (segment[0] == '0' and len(segment) > 1) or
        int(segment) > 255
    )

class Solution(object):
    def restoreIpAddresses(self, s):
        solution = []

        def dfs(index, segments):
            # base case: too many segments
            if len(segments) > 4:
                return

            # base case: valid IP
            if index == len(s) and len(segments) == 4:
                solution.append(".".join(segments))
                return

            # try segments of length 1 to 3
            for length in range(1, 4):
                if index + length > len(s):
                    break
                segment = s[index:index + length]
                if checkInvalidSegment(segment):
                    continue
                dfs(index + length, segments + [segment])

        dfs(0, [])
        return solution

# # base case 1: IP address is invalid -> just return out
# # base case 2: IP address is valid, and fully complete -> append to solution list and return

# def checkInvalidIP(ip_addr):
#     integers = ip_addr.split(".")
#     if len(integers) != 4:
#         return True

#     for integer in integers:
#         if integer == '' or (integer[0] == '0' and len(integer) > 1) or int(integer) > 255:
#             return True
    
#     return False

# class Solution(object):
#     def restoreIpAddresses(self, s):
#         """
#         :type s: str
#         :rtype: List[str]
#         """
#         solution = []
#         address = ""

#         def dfs(address, index):
#             # base cases
#             if index >= len(s) and checkInvalidIP(address[:-1]):
#                 return
#             elif index >= len(s) and not checkInvalidIP(address[:-1]):
#                 solution.append(address[:-1])
#                 return
            
#             # recursive case
#             # case 1: next character and decimal point
#             next_decimal = s[index] + "."
#             address += next_decimal
#             dfs(address, index + 1)
#             address = address[:-2]

#             # case 2: next two characters and decimal point
#             next_decimal = s[index:(index + 2)] + "."
#             address += next_decimal
#             dfs(address, index + 2)
#             address = address[:-3]

#             # case 3: next three characters and decimal point
#             next_decimal = s[index:(index + 3)] + "."
#             address += next_decimal
#             dfs(address, index + 3)
#             address = address[:-4]

#         dfs(address, 0)
#         return solution