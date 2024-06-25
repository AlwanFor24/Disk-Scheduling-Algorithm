import matplotlib.pyplot as plt

# Constants
HIGH = 199
LOW = 0
RPM = 7200  # Rotations per minute
SECTORS = 200  # Number of sectors per track

def calculate_rotational_delay(sectors_per_track):
    # Satu Rotasi ( milliseconds)
    rotation_time_ms = 60000 / RPM
    # Rotational delay ( Setengah Rotasi )
    return rotation_time_ms / 2

def main():
    seek = 0
    rotational_delay = 0

    #Input track
    q_size = int(input("Input jumlah disk locations: "))
    head = int(input("Input initial head position: "))


    if head < LOW or head > HIGH:
        print(f"Error: Initial head position must be between {LOW} and {HIGH}.")
        return

    # Menkodisikan berrdasarkan waktu arrival
    queue = []
    print("Enter disk positions to be read in the order of their arrival:")
    for _ in range(q_size):
        while True:
            temp = int(input())
            if LOW <= temp <= HIGH:
                queue.append(temp)
                break
            else:
                print(f"Error: Disk Position harus berada pada rentang  {LOW} and {HIGH}.")

    #insert to queue
    queue.insert(0, head)

    #buat chart
    seek_times = [0]  #inisiasi seek time di head
    positions = [head]

    # Hitung seek times and rotational delays
    for j in range(len(queue) - 1):
        diff = abs(queue[j + 1] - queue[j])
        seek += diff
        rotational_delay += calculate_rotational_delay(SECTORS)
        positions.append(queue[j + 1])
        seek_times.append(seek)

        print(f"Disk head moves from {queue[j]} -> {queue[j + 1]} with seek {diff}")

    # Hitung total dan rata-rata total and average delays
    total_delay = seek + rotational_delay
    avg_seek_time = seek / q_size
    avg_rotational_delay = rotational_delay / q_size
    avg_total_delay = total_delay / q_size


    print(f"Total seek time = {seek}")
    print(f"Total rotational delay = {rotational_delay:.2f} ms")
    print(f"Total acces time (seek time + rotational delay) = {total_delay:.2f}")
    print(f"Average seek time = {avg_seek_time:.2f}")
    print(f"Average rotational delay = {avg_rotational_delay:.2f} ms")
    print(f"Average total acces time = {avg_total_delay:.2f}")

    # Plotting the movements with swapped coordinates
    plt.figure(figsize=(10, 5))
    plt.plot(seek_times, positions, marker='o')
    plt.title("FIFO Disk Scheduling")
    plt.xlabel("Accumulated Seek Time")
    plt.ylabel("Disk Position")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
