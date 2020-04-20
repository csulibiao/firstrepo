from queue import PriorityQueue as PQ


if __name__ == "__main__":
    # 读取第一行的n
    # n = int(sys.stdin.readline().strip())
    records = [['China', '53','20','21'],
               ['Bmer', '53','20','21'],
               ['Japan', '54','0','0'],
               ['Japaz', '54','0','1']
             ]
    pq = PQ() #使用优先队列，
    for record in records:
        name = record[0]
        score = 40000*int(record[1])+200*int(record[2])+int(record[3])
        pq.put((-score,name)) #优先队列默认从小到大排序，所以需要取负值
    for i in range(len(records)):
        print(pq.get()[1])
