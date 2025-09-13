#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <list>
int solve(int idx, int total_height) {
    extern int min_answer;
    extern int N, B;
    extern std::list<int> heights;

    if(total_height > B)
    {
        min_answer = std::min(min_answer, total_height);
    }

    if(idx == N)
    {
        return;
    }
    auto it = heights.begin();
    std::advance(it, idx);
    solve(idx + 1, total_height + *it);
    solve(idx + 1, total_height);
}

int main(int argc, char** argv)
{
    int test_case;
    int T; // T : 테스트 케이스 개수

    freopen("high_shelf_input.txt", "r", stdin);
	freopen("high_shelf_output.txt", "w", stdout);

    std::cin>>T;

    for(test_case = 1; test_case <= T; ++test_case)
    {	
        int N, B; // N : 점원의 수, B : 점원의 키
        std::list<int> height; // 점원 키 리스트
        int min_answer = 10000 * N;
	
        solve(0, 0);

        std::cout << "# " << test_case << min_answer - B << std::endl;
	};
	return ;
}