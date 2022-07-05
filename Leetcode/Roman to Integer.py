# Given a roman numeral, convert it to an integer.
#Time: O(n)
#Space: O(128) = O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for a, b in zip(s, s[1:]):
            if roman[a] < roman[b]:
                ans -= roman[a]
            else:
                ans += roman[a]

        return ans + roman[s[-1]]






# Time complexity of O(1), but slower due to using more if-else statements than the above.

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0

        # Dictionary where keys are the Roman Numerals. Values are the corresponding int.
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,'M': 1000}
        
        # list out keys and values separately.
        key_list = list(roman_dict.keys())
        val_list = list(roman_dict.values())
        
        for i, v in enumerate(s):
            position = key_list.index(v)
            k = i + 1 if i != len(s) - 1 else -1
            if v == "I":
                if s[k] == 'V':
                   # if i != 0:
                    total = total - 1 
                elif s[k] == 'X':
                    total = total - 1 
                else:
                    total += val_list[position]

            elif v == "X":
                if s[k] == 'L':
                    total = total - 10 
                elif s[k] == 'C':
                    total = total - 10
                else:
                    total += val_list[position]
                    
            elif v == "C":
                if s[k] == 'D':
                    total = total - 100 
                elif s[k] == 'M':
                    total = total - 100
                else:
                    total += val_list[position]
                       
            else:
                total += val_list[position]
            print(total)
        return(total)        

        
