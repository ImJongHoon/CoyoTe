# def main():
#     num = int(input())
#     # schedule = [[-1, -1] for _ in range(num+1)]

#     # for _ in range(num):
#     #     (cor_num, start_time, end_time) = map(int, input().split())
#     #     #0을 비워두고 입력받았음.
#     #     schedule[cor_num][0] = start_time
#     #     schedule[cor_num][1] = end_time


#     schedule = [tuple(map(int, input().split())) for _ in range(num)]

#     # print(schedule)

#     # 문제가 좀 불명확한듯?
#     # 출력은 첫번째 강의 번호부터 어디 강의실에 배정되었는지 확인
#     # 강의실 번호를 할당하는 기준이 뭔데. 앞에서부터?
#     # 질문 게시판을 참고하니 아래와 같이 같은 예시에 다른 번호를 할당해도 상관 없었음.
#     # 5
#     # 2
#     # 5
#     # 1
#     # 2
#     # 4
#     # 5
#     # 1
#     # 3
    
#     sorted_schedule = sorted(schedule, key=lambda x: x[2] - x[1], reverse=True)
#     # print(sorted_schedule)

#     # 배정하고 확인하면 되는거 아님?
#     total = 1
#     for info in sorted_schedule:
#         #이전에 나왔던 애들을 모두 확인해야하기 때문에 O(n^2)임
#         pass



# if __name__ == "__main__":
#     main()

# 힙 따로 관리하지마
# import heapq

# def main():
#     num = int(input())

#     schedule = [tuple(map(int, input().split())) for _ in range(num)]
    
#     sorted_schedule = sorted(schedule, key=lambda x: x[1])

#     room_heapq_list = []

#     room_max_cnt = 1
#     for info in sorted_schedule:
#         # 비어있으면
#         if not room_heapq_list:
#             # 시작 순서대로 오기 때문에 시작은 고려할 필요 없음. 더 빨리 시작하는 애가 없기 때문.
#             # heap은 첫번째 요소로 비교하도록 고정됨
#             room_heapq_list.append([])
#             heapq.heappush(room_heapq_list[room_max_cnt-1], (info[2], room_max_cnt, info[0]))
#             # print(room_heapq)
#         # 2차원 배열인 셈
#         isEmpty = False
#         for idx in range(room_max_cnt):
#             # info[1] 이 시작 시간 [2]가 끝나는 시간 [0]이 몇번 강의인지
#             # print(room_heapq_list[idx])
#             # 튜플 맨 앞의 값이 가장 작은 첫번째 요소의, 첫번째 값(끝나는 시간)
#             if room_heapq_list[idx][0][0] <= info[1]:
#                 heapq.heappush(room_heapq_list[idx], (info[2], idx+1, info[0]))
#                 isEmpty = True
#                 break

#         #할당 못 받음
#         if isEmpty == False:
#             room_max_cnt += 1
#             room_heapq_list.append([])
#             heapq.heappush(room_heapq_list[room_max_cnt-1], (info[2], room_max_cnt, info[0]))
    
#     # 강의 번호 기준으로 정렬해야됨.
#     # room_result_list = []
#     print(room_heapq_list)
#     # 바보임
#     # for li in room_heapq_list:
#     #     room_result_list.append(li)
    
#     # 배열 병합 빠른 코드
#     room_result_list = [elem for li in room_heapq_list for elem in li]

#     room_result_list.sort(key=lambda x: x[2])

#     print(room_max_cnt)
#     for info in room_result_list:
#         print(info[1])


# if __name__ == "__main__":
#     main()



import heapq

def main():
    num = int(input())

    schedule = [tuple(map(int, input().split())) for _ in range(num)]
    
    sorted_schedule = sorted(schedule, key=lambda x: x[1])

    room_heapq_list = []

    room_cnt = 0

    room_assign = [0] * (num + 1)

    for lect_num, start, end in sorted_schedule:
        room_num = -1
        # 가장 빨리 끝나는애가 버블처럼 올라오는 구조임
        if room_heapq_list and room_heapq_list[0][0] <= start:
            recent_end, room_num = heapq.heappop(room_heapq_list)
        
        else:
            room_cnt += 1
            room_num = room_cnt
        
        heapq.heappush(room_heapq_list, (end, room_num))
        room_assign[lect_num] = room_num
    
    print(room_cnt)
    for i in range(1, num+1):
        print(room_assign[i])


if __name__ == "__main__":
    main()