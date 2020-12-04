room_no = int(input('Room: '))
print('Status: safe') if(room_no == int(str(room_no**2)[:len(str(room_no**2))//2])+int(str(room_no**2)[len(str(room_no**2))//2:])) else print('Status: Not safe')