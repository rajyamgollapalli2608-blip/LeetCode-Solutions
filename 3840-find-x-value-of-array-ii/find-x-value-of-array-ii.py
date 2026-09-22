class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # Each node stores:
        # prod = product of the whole segment modulo k
        # cnt[r] = number of non-empty prefixes of this segment
        #          whose product % k == r

        size = 1
        while size < n:
            size *= 2

        prod = [1] * (2 * size)
        cnt = [[0] * k for _ in range(2 * size)]

        def make_leaf(value):
            p = value % k
            c = [0] * k
            c[p] = 1
            return p, c

        def merge(left_prod, left_cnt, right_prod, right_cnt):
            # Product of complete merged segment
            new_prod = (left_prod * right_prod) % k

            new_cnt = [0] * k

            # Prefixes completely inside the left segment
            for r in range(k):
                new_cnt[r] += left_cnt[r]

            # Prefixes that:
            # 1. take the whole left segment
            # 2. then take a prefix of the right segment
            for r in range(k):
                if right_cnt[r]:
                    new_r = (left_prod * r) % k
                    new_cnt[new_r] += right_cnt[r]

            return new_prod, new_cnt

        # Build leaves
        for i in range(n):
            p, c = make_leaf(nums[i])
            prod[size + i] = p
            cnt[size + i] = c

        # Build tree
        for i in range(size - 1, 0, -1):
            prod[i], cnt[i] = merge(
                prod[2 * i],
                cnt[2 * i],
                prod[2 * i + 1],
                cnt[2 * i + 1]
            )

        def update(index, value):
            pos = size + index

            prod[pos], cnt[pos] = make_leaf(value)

            pos //= 2

            while pos:
                prod[pos], cnt[pos] = merge(
                    prod[2 * pos],
                    cnt[2 * pos],
                    prod[2 * pos + 1],
                    cnt[2 * pos + 1]
                )
                pos //= 2

        def query(left, right):
            """
            Returns:
                product of nums[left:right+1] modulo k
                counts of products of all non-empty prefixes
            """

            # Empty left/right parts
            left_prod = 1
            left_cnt = [0] * k

            right_prod = 1
            right_cnt = [0] * k

            l = left + size
            r = right + size + 1

            while l < r:
                if l % 2 == 1:
                    left_prod, left_cnt = merge(
                        left_prod,
                        left_cnt,
                        prod[l],
                        cnt[l]
                    )
                    l += 1

                if r % 2 == 1:
                    r -= 1
                    right_prod, right_cnt = merge(
                        prod[r],
                        cnt[r],
                        right_prod,
                        right_cnt
                    )

                l //= 2
                r //= 2

            # Combine the two parts
            return merge(
                left_prod,
                left_cnt,
                right_prod,
                right_cnt
            )

        result = []

        for index, value, start, x in queries:

            # Persistent update
            update(index, value)

            # We need all possible non-empty prefixes
            # of nums[start:]
            _, counts = query(start, n - 1)

            result.append(counts[x])

        return result