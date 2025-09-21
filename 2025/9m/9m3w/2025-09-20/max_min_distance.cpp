#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath> 

int main(int argc, char** argv)
{
    freopen("max_min_distance_input.txt", "r", stdin);

    int test_case;
    int T, N;
    int max_index, min_index ;

    std::cin >> T;

    for (test_case = 1; test_case <= T; ++test_case)
    {
        std::cin >> N;

        // 1. �ùٸ� vector ����: ũ�� N�� ������ ��ȣ ()�� ����
        std::vector<int> arr(N);

        // 2. �ùٸ� vector �Է�: �ݺ������� �� ���� arr[i]�� ���� �Է�
        for (int i = 0; i < N; i++) {
            std::cin >> arr[i];
        }

        std::cout << "#" << test_case << " ";
        // �Է� Ȯ�ο� ���
        for (int i = 0; i < arr.size(); i++) {
            if(arr[i] < arr[min_index]){
                min_index = i;
            }
            if(arr[i] >= arr[max_index]){
                max_index = i;
            }
        }
        std::cout << abs(max_index - min_index) << std::endl; // 3. �����ݷ� �߰� �� �ٹٲ�
    }
    return 0;
}