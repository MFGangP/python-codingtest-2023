#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <cstdio>

int main(int argc, char** argv)
{
    int test_case;
    int T, N;

    std::cin >> T;

    for (test_case = 1; test_case <= T; ++test_case)
    {
        std::cin >> N;

        // 1. 올바른 vector 선언: 크기 N을 생성자 괄호 ()에 전달
        std::vector<int> arr(N);

        // 2. 올바른 vector 입력: 반복문으로 각 원소 arr[i]에 직접 입력
        for (int i = 0; i < N; i++) {
            std::cin >> arr[i];
        }

        std::cout << "#" << test_case << " ";
        // 입력 확인용 출력
        for (int i = 0; i < arr.size(); i++) {
            std::cout << arr[i] << " ";
        }
        std::cout << std::endl; // 3. 세미콜론 추가 및 줄바꿈
    }
    return 0;
}