class Solution:
    # Save outer layer, calculate inner layer, and go back to out layer
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        cur_num = 0
        cur_str = ""

        for ch in s:
            # Update number by dealing with multi-digit numbers
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            
            # Update string by concatenation
            elif ch.isalpha():
                cur_str += ch

            # "[" is the sign of saving outer layer and focusing inner layer
            # After saving, reset cur_num and cur_str for inner layer
            elif ch == "[":
                num_stack.append(cur_num)
                str_stack.append(cur_str)
                cur_num = 0
                cur_str = ""

            # "]" is the sign of invoking outer layer and combing it with current string
            elif ch == "]":
                k = num_stack.pop()
                prev_str = str_stack.pop()
                cur_str = prev_str + k * cur_str
            
        return cur_str

            