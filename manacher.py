def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    slist='#'.join(s)
    slist= '#'+slist+'#'
    index=-1
    pR=-1
    maxR=0
    pArr=[0 for i in xrange(len(slist))]
    for i in xrange(len(slist)):
        pArr[i]=min(pArr[2*index-i],pR-i) if pR>i else  1
        while i+pArr[i]<len(slist) and i-pArr[i]>-1:
            if slist[i+pArr[i]]==slist[i-pArr[i]]:
                pArr[i]+=1
            else:
                break
        if i+pArr[i]>pR:
            pR= i+pArr[i]
            index=i;
        maxR = max(pArr[i],maxR)
    indexR= pArr.index(maxR)
    maxR = maxR - 1
    center = indexR/2
    R = maxR / 2
    if indexR &1:
        return s[center - R:center + R+1]
    else:
        return s[center - R:center + R]
print longestPalindrome("abc1234321ab")


