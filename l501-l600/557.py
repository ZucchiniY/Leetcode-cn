class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split(' ')
        st = []
        for ss in str_list:
            st.append(ss[::-1])
        return ' '.join(st)
