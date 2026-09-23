def longestPalindrome(s: str) -> str:
    def expand(l, r)-> str:
        while 0 <= l <= r < len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1: r]
    pals = [expand(i,i) for i in range(len(s))] + [expand(i,i+1) for i in range(len(s)-1) if s[i]==s[i+1]]
    return max(pals, key=len) if len(pals) > 0 else ''

if __name__ == "__main__":
    assert longestPalindrome("abbcccba") == "bcccb"
    assert longestPalindrome("cbbd") == "bb"
    assert longestPalindrome("babad") == "bab"
