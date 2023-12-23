def calculate_acceleration(initial_velocity, final_velocity, time):
    # Menghitung perubahan kecepatan
    delta_velocity = final_velocity - initial_velocity
    
    # Menghitung percepatan
    acceleration = delta_velocity / time
    
    return acceleration

# Memasukkan data dari pengguna
initial_velocity = float(input("Masukkan kecepatan awal (m/s): "))
final_velocity = float(input("Masukkan kecepatan akhir (m/s): "))
time = float(input("Masukkan waktu (s): "))

# Memanggil fungsi untuk menghitung percepatan
result_acceleration = calculate_acceleration(initial_velocity, final_velocity, time)

# Menampilkan hasil
print(f"Percepatan benda adalah {result_acceleration} m/s^2.")
