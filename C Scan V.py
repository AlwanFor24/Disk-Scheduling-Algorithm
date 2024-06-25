HIGH = 199
LOW = 0
ROTATIONAL_DELAY = 4  # Assumed average rotational delay in milliseconds

def main():
    queue1 = []
    queue2 = []
    seek = 0
    rotational_delay = 0

    q_size = int(input("Input no of disk locations: "))
    head = int(input("Enter initial head position: "))

    print("Enter disk positions to be read")
    for _ in range(q_size):
        temp = int(input())
        if temp >= head:
            queue1.append(temp)
        else:
            queue2.append(temp)

    # Sort both lists
    queue1.sort()
    queue2.sort()

    queue = []

    # Calculate closest edge
    if abs(head - LOW) >= abs(head - HIGH):
        queue = [head] + queue1 + [HIGH, LOW] + queue2
    else:
        queue = [head] + queue2[::-1] + [LOW, HIGH] + queue1[::-1]

    for j in range(len(queue) - 1):
        diff = abs(queue[j + 1] - queue[j])
        seek += diff
        rotational_delay += ROTATIONAL_DELAY
        print(f"Disk head moves from {queue[j]} to {queue[j + 1]} with seek {diff} and rotational delay {ROTATIONAL_DELAY}ms")

    total_time = seek + rotational_delay
    print(f"Total seek time is {seek}")
    print(f"Total rotational delay is {rotational_delay}ms")
    avg_seek_time = seek / q_size
    avg_rotational_delay = rotational_delay / q_size
    print(f"Average seek time is {avg_seek_time:.2f}")
    print(f"Average rotational delay is {avg_rotational_delay:.2f}ms")
    print(f"Total time (seek time + rotational delay) is {total_time}ms")

if __name__ == "__main__":
    main()


def main():
    queue1 = []
    queue2 = []
    seek = 0
    rotational_delay = 0

    q_size = int(input("Input no of disk locations: "))
    head = int(input("Enter initial head position: "))

    print("Enter disk positions to be read")
    for _ in range(q_size):
        temp = int(input())
        if temp >= head:
            queue1.append(temp)
        else:
            queue2.append(temp)

    # Sort both lists
    queue1.sort()
    queue2.sort()

    queue = []

    # Calculate closest edge
    if abs(head - LOW) >= abs(head - HIGH):
        queue = [head] + queue1 + [HIGH, LOW] + queue2
    else:
        queue = [head] + queue2[::-1] + [LOW, HIGH] + queue1[::-1]

    for j in range(len(queue) - 1):
        diff = abs(queue[j + 1] - queue[j])
        seek += diff
        rotational_delay += ROTATIONAL_DELAY
        print(f"Disk head moves from {queue[j]} to {queue[j + 1]} with seek {diff} and rotational delay {ROTATIONAL_DELAY}ms")

    total_time = seek + rotational_delay
    print(f"Total seek time is {seek}")
    print(f"Total rotational delay is {rotational_delay}ms")
    avg_seek_time = seek / q_size
    avg_rotational_delay = rotational_delay / q_size
    print(f"Average seek time is {avg_seek_time:.2f}")
    print(f"Average rotational delay is {avg_rotational_delay:.2f}ms")
    print(f"Total time (seek time + rotational delay) is {total_time}ms")

if __name__ == "__main__":
    main()
