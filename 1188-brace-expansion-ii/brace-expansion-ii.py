class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:

        i = 0

        def parse():
            nonlocal i

            result = set()

            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    i += 1
                    current = parse()
                    i += 1
                else:
                    current = {expression[i]}
                    i += 1

                if result:
                    result = {a + b for a in result for b in current}
                else:
                    result = current

                if i < len(expression) and expression[i] == ',':
                    i += 1
                    result |= parse()

            return result

        return sorted(parse())