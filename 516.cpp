#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
  int longestPalindromeSubseq(string s) {
	if (s.length() == 0)
	  return 0;

	int length = s.length();
    int matrix[length][length+1];

	for (int i = 0; i < length; ++i) {
	  matrix[i][0] = 0;
	  matrix[i][1] = 1;
	}

	// dp
	int ret = 1;
	for (int subLen = 2; subLen < length+1; ++subLen) {
	  for (int start = 0; start < length - subLen + 1; ++start) {
		if (s[start] == s[start + subLen - 1]) {
		  matrix[start][subLen] = matrix[start + 1][subLen - 2] + 2;
		}
		else {
		  matrix[start][subLen] = max(matrix[start + 1][subLen - 1], matrix[start][subLen - 1]);
		}

		if (ret < matrix[start][subLen])
		  ret = matrix[start][subLen];

	  }
	}

	return ret;
  }
};

int main(void) {
  Solution *sol = new Solution();
    
  cout << sol->longestPalindromeSubseq("cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc") << endl;
  cout << sol->longestPalindromeSubseq("bbbab") << endl;
}
