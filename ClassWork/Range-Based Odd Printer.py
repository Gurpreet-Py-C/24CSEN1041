start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
stop_at = int(input("Stop at: "))
if start >= end:
    print("Invalid range: start must be less than end.")
elif not (start <= stop_at < end):
    print("Invalid stop value: must be within the range.")
else:
    for i in range(start, end):
        if i == stop_at:
            if i % 2 != 0:
                print(i)
            break
        if i % 2 != 0:
            print(i)
