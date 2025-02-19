class Solution {
public:
    string smallestNumber(string pattern) {
        int n=pattern.length();
        int counter=1;
        string num="";
        stack<char>st;

        for(int i=0;i<=n;i++){
            st.push(counter+'0');
            counter++;
            if(pattern[i]=='I' || i==n){
                while(!st.empty()){
                    char top=st.top();
                    st.pop();
                    num+=top;
                }
            }
        }
        return num;
    }
};