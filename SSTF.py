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


def sstf_scheduling(requests, head):
    seek_sequence = [head]
    total_seek = 0
    total_rotational_delay = 0

    while requests:
       # Menentukan track terdekat dari track saat ini
        closest_request = min(requests, key=lambda x: abs(x - head))
        seek_distance = abs(closest_request - head)

        #  total seek and rotational delay
        total_seek += seek_distance
        total_rotational_delay += calculate_rotational_delay(SECTORS)

        # Tracking ke track terdekat
        head = closest_request
        seek_sequence.append(head)

        # Remove the processed request == Buat mencegah kembali ke sebelumnya apabila seek time
        #  menuju track selanjutnya lebih besar
        requests.remove(closest_request)

        print(f"Disk  from {seek_sequence[-2]} -> {seek_sequence[-1]}  seek time = {seek_distance}")

    return seek_sequence, total_seek, total_rotational_delay


def main():
    requests = []
    seek = 0
    rotational_delay = 0

    q_size = int(input("Input jumlah disk position : "))
    head = int(input("Input initial head position: "))

    if head < LOW or head > HIGH:
        print(f"Error: Initial Head harus berada pada rentang  {LOW} and {HIGH}.")
        return

    print("Input disk position : ")
    for _ in range(q_size):
        while True:
            temp = int(input())
            if LOW <= temp <= HIGH:
                requests.append(temp)
                break
            else:
                print(f"Error: Disk Position tidak bisa diinput. Disk Position harus berada pada rentang  {LOW} and {HIGH}.")

    seek_sequence, total_seek, total_rotational_delay = sstf_scheduling(requests, head)

    total_delay = total_seek + total_rotational_delay
    avg_seek_time = total_seek / q_size
    avg_rotational_delay = total_rotational_delay / q_size
    avg_total_delay = total_delay / q_size

    print(f"Total seek time = {total_seek}")
    print(f"Total rotational delay = {total_rotational_delay:.2f} ms")
    print(f"Total acces time (seek time + rotational delay) is {total_delay:.2f}")
    print(f"Average seek time = {avg_seek_time:.2f}")
    print(f"Average rotational delay = {avg_rotational_delay:.2f} ms")
    print(f"Average acces time = {avg_total_delay:.2f}")


    seek_times = [0]
    accumulated_seek = 0

    #Akumulasi seek time
    for i in range(1, len(seek_sequence)):
        accumulated_seek += abs(seek_sequence[i] - seek_sequence[i - 1])
        seek_times.append(accumulated_seek)

    plt.figure(figsize=(10, 5))
    plt.plot(seek_times, seek_sequence, marker='o')
    plt.title("SSTF Disk Scheduling")
    plt.xlabel("Total Seek Time")
    plt.ylabel("Disk Position")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
