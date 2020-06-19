n = int(input())
A = [int(i) for i in input().split()]

assert (1 <= n <= 10 ** 6)
assert (all([1 <= x <= 9 for x in A]))

M = 10 ** 9 + 7

curSum, curSumFromVertex, curVertexCount, height = 0, 0, 1, 0
for a in A:
    newYSum = (curSumFromVertex + a * curVertexCount) * 2 + (curSumFromVertex + 2 * a * curVertexCount) * 2 + a
    newSumFromVertex = curSumFromVertex + (curSumFromVertex + (height + 2 * a) * curVertexCount) + \
                             2 * (curSumFromVertex + (height + 3 * a) * curVertexCount) + height + a + height + 2 * a
    newSum1 = 2 * (2 * curSumFromVertex * curVertexCount + 2 * a * curVertexCount * curVertexCount)
    newSum2 = 4 * (2 * curSumFromVertex * curVertexCount + 3 * a * curVertexCount * curVertexCount)
    curSum = newSum1 + newSum2 + newYSum * 2 - a + curSum * 4
    curSumFromVertex = newSumFromVertex
    height = height * 2 + 3 * a
    curVertexCount = curVertexCount * 4 + 2
    curSum %= M
    curSumFromVertex %= M
    curVertexCount %= M
    height %= M

print (curSum)
