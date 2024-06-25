import matplotlib.pyplot as plt

HIGH = 200
LOW = 0
RPM = 7200  # Rotations per minute
SECTORS = 200  # Number of sectors per track

def calculate_rotational_delay(sectors_per_track):
    # Satu Rotasi ( milliseconds)
    rotation_time_ms = 60000 / RPM
    # Rotational delay ( Setengah Rotasi )
    return rotation_time_ms / 2

def main():
    queue1 = []
    queue2 = []
    seek = 0
    rotational_delay = 0

    q_size = int(input("Input jumlah of disk locations: "))
    head = int(input("Input initial head position: "))

    if head <= LOW or head >= HIGH:
        print(f"Error: Initial Head harus berada pada rentang  {LOW} and {HIGH}.")
        return

    print("Input disk positions : ")
    for _ in range(q_size):
        while True:
            temp = int(input())
            if LOW < temp < HIGH:
                if temp >= head:
                    queue1.append(temp)
                else:
                    queue2.append(temp)
                break
            else:
                print(f"Error: Initial Head harus berada pada rentang  {LOW} and {HIGH}.")

    # Sort both lists
    queue1.sort() #buat track naik dari head
    queue2.sort() #buat track terkecil ke head setelah track maksimum

    queue = []

    # if 1: memproses track naik , if 2 : memproses dari track awal ke head ( ::-1 ) == reverse order
    if abs(head - LOW) >= abs(head - HIGH):
        queue = [head] + queue1 + queue2
    else:
        queue = [head] + queue2[::-1] + queue1[::-1]

    seek_times = [0] # inisiasi seek time di head
    positions = [head]

    for j in range(len(queue) - 1):
        diff = abs(queue[j + 1] - queue[j])
        seek += diff
        rotational_delay += calculate_rotational_delay(SECTORS)
        positions.append(queue[j + 1])
        seek_times.append(seek)

        print(f"Disk from {queue[j]} -> {queue[j + 1]} seek time = {diff}")

    total_delay = seek + rotational_delay
    print(f"Total seek time = {seek}")
    print(f"Total rotational delay = {rotational_delay:.2f} ms")
    print(f"Total acces time (seek time + rotational delay) = {total_delay:.2f}")
    avg_seek_time = seek / q_size
    avg_rotational_delay = rotational_delay / q_size
    avg_total_delay = avg_seek_time + avg_rotational_delay
    print(f"Average seek time = {avg_seek_time:.2f}")
    print(f"Average rotational delay = {avg_rotational_delay:.2f} ms")
    print(f"Average acces time = {avg_total_delay:.2f}")


    plt.figure(figsize=(10, 5))
    plt.plot(seek_times, positions, marker='o')
    plt.title("C-Scan Disk Scheduling")
    plt.xlabel("Accumulated Seek Time")
    plt.ylabel("Disk Position")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
