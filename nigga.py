

with open("niggas.txt","r") as f:
    list_a = []
    list_b = []

    lines = f.readlines()
    result = 0
    for line in lines:

        line = line.strip().replace(" ", "")
        iter_num =  len(line) / 2
        iter_num = int(iter_num)
        nums = iter(list(line))
        for i in range(iter_num):
            list_a.append(next(nums))
        
        for i in range(iter_num):
            list_b.append(next(nums))  
    
    list_a_str = ''.join(list_a)
    list_b_str = ''.join(list_b)
    
    a_chunks = []
    b_chunks = []
    for i in range(0, len(list_a_str), 5):
        a_chunks.append(list_a_str[i:i+5])
        b_chunks.append(list_b_str[i:i+5])
    # ITERATE OVER A COPY OF THE LIST, SO THAT IT DOESN'T STOP AFTER A CERTAIN NUMBER! ! ! ! !
    for i in a_chunks[:]:
        a = int(min(a_chunks))
        b = int(min(b_chunks))
        
        result += abs(a - b)

        a_chunks.remove(str(a))
        b_chunks.remove(str(b))

    print(result)
