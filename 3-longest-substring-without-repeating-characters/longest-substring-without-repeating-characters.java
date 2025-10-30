class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int maxLen = 0;

        Set<Character> set1 = new HashSet<>();
        for (int right = 0; right< s.length(); right++){
            char c = s.charAt(right);
            while(set1.contains(c)){
                set1.remove(s.charAt(left));
                left++;
            }
            set1.add(c);
            maxLen = Math.max(maxLen,right-left+1);
        }
        return maxLen;
    }
}

