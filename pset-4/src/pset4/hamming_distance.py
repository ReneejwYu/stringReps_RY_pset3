def hammingDistance(p: str, q: str) -> int:
    mismatch = 0

    for i in range(len(p)):
        if p[i] != q[i]:
            mismatch += 1

    return mismatch