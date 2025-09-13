#include <iostream>
#include <vector>     // list 대신 vector 사용
#include <algorithm>  // min 함수 사용
#include <stdio.h>    // freopen 함수 사용

// 1. 변수들을 main 밖으로 빼서 '전역 변수'로 만듭니다.
// 이렇게 하면 모든 함수(main, solve)에서 접근할 수 있습니다.
int N, B;
std::vector<int> heights; // 2. 효율적인 vector로 변경
int min_answer;

// 3. 반환값이 없으므로 void 타입으로 변경
void solve(int idx, int total_height) {
    // 4. 전역 변수를 사용하므로 extern 선언은 필요 없습니다.

    // 5. 로직 오류 수정 ('>' -> '>=')
    if (total_height >= B) {
        min_answer = std::min(min_answer, total_height);
        return; // 가지치기: 이미 B를 넘었으면 더 깊이 들어가지 않고 종료
    }

    if (idx == N) {
        return; // 모든 점원을 확인했으면 종료
    }

    // 6. vector는 인덱스로 바로 접근하여 훨씬 빠릅니다.
    solve(idx + 1, total_height + heights[idx]); // 현재 점원을 탑에 포함
    solve(idx + 1, total_height);                // 현재 점원을 탑에 미포함
}

int main(int argc, char** argv) {
    // 입출력 속도 향상 (알고리즘 문제 풀 때 추천)
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    freopen("high_shelf_input.txt", "r", stdin);
    freopen("high_shelf_output.txt", "w", stdout);

    int T;
    std::cin >> T;

    for (int test_case = 1; test_case <= T; ++test_case) {
        // 7. 입력 코드를 추가합니다.
        std::cin >> N >> B;

        // vector 크기를 N으로 설정하고, height 값을 입력받습니다.
        heights.assign(N, 0); // vector를 N개의 0으로 초기화
        for (int i = 0; i < N; ++i) {
            std::cin >> heights[i];
        }

        // 8. N값을 입력받은 후에 min_answer를 초기화합니다.
        min_answer = 987654321; // 나올 수 있는 값보다 충분히 큰 수로 초기화

        solve(0, 0);

        // 출력 형식 맞춤
        std::cout << "#" << test_case << " " << min_answer - B << "\n";
    }

    return 0; // 9. 세미콜론 추가
}