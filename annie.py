import subprocess
from colorama import init, Fore, Style
from tqdm import tqdm
import time
import os

# Inisialisasi colorama
init(autoreset=True)

def print_header():
    # Header ASCII Art
    header = r"""
     _    _ _   _ _             
    / \  | | | | (_)            
   / _ \ | | | | |_ _ __   __ _  
  / ___ \| | | | | | '_ \ / _` | 
 /_/   \_\_| |_|_|_| | | | (_| | 
                    |_| |_|\__,_| 
    """
    print(Fore.CYAN + header)
    print(Fore.MAGENTA + Style.BRIGHT + "coded by D A N Z")
    print(Style.RESET_ALL)

def run_nuclei():
    while True:
        print_header()

        # Meminta input URL target dari user
        target_url = input(Fore.YELLOW + "Masukkan URL target (contoh: http://target.com): ")

        # Meminta input opsi perintah Nuclei dari user
        print("\n" + Fore.CYAN + "Pilih opsi perintah Nuclei:")
        print(Fore.CYAN + Style.BRIGHT + "+---+-----------------------------------------------+")
        print(Fore.CYAN + Style.BRIGHT + "| 1 | -silent (Hanya menampilkan hasil kerentanan)   |")
        print(Fore.CYAN + Style.BRIGHT + "| 2 | -severity (Memilih tingkat keparahan)          |")
        print(Fore.CYAN + Style.BRIGHT + "| 3 | -t (Menggunakan template tertentu)             |")
        print(Fore.CYAN + Style.BRIGHT + "| 4 | Tanpa opsi (Default scan)                      |")
        print(Fore.CYAN + Style.BRIGHT + "+---+-----------------------------------------------+")
        opsi = input(Fore.YELLOW + "Masukkan nomor opsi (1/2/3/4): ")

        # Menentukan perintah sesuai pilihan user
        if opsi == "1":
            nuclei_command = ["nuclei", "-u", target_url, "-silent"]
        elif opsi == "2":
            severity_level = input(Fore.YELLOW + "Masukkan tingkat keparahan (contoh: low,medium,high,critical): ")
            nuclei_command = ["nuclei", "-u", target_url, "-severity", severity_level]
        elif opsi == "3":
            template_path = input(Fore.YELLOW + "Masukkan path atau nama template (contoh: cves/2021/CVE-2021-12345.yaml): ")
            nuclei_command = ["nuclei", "-u", target_url, "-t", template_path]
        else:
            nuclei_command = ["nuclei", "-u", target_url]

        # Meminta user untuk memilih output
        print("\n" + Fore.CYAN + "Pilih output:")
        print(Fore.CYAN + Style.BRIGHT + "+---+-----------------------------------------------+")
        print(Fore.CYAN + Style.BRIGHT + "| 1 | Tampilkan langsung di terminal                |")
        print(Fore.CYAN + Style.BRIGHT + "| 2 | Simpan dalam file txt                         |")
        print(Fore.CYAN + Style.BRIGHT + "+---+-----------------------------------------------+")
        output_choice = input(Fore.YELLOW + "Masukkan nomor pilihan output (1/2): ")

        # Menampilkan progress bar
        print(Fore.GREEN + "\nMenjalankan pemindaian...\n")
        for i in tqdm(range(100), desc="Progress", bar_format="{l_bar}{bar} [time left: {remaining}]"):
            time.sleep(0.03)  # Simulasi loading

        # Menjalankan perintah sesuai pilihan output
        if output_choice == "1":
            result = subprocess.run(nuclei_command, text=True)
            print(Fore.GREEN + "\nPemindaian selesai.")
        elif output_choice == "2":
            output_file = input(Fore.YELLOW + "Masukkan nama file untuk menyimpan hasil (contoh: hasil-pemindaian.txt): ")
            nuclei_command.extend(["-o", output_file])
            result = subprocess.run(nuclei_command, text=True)
            print(Fore.GREEN + f"\nPemindaian selesai. Hasil disimpan dalam file {output_file}.")
        else:
            print(Fore.RED + "Pilihan output tidak valid.")

        # Prompt untuk menjalankan scan lagi
        scan_again = input(Fore.YELLOW + "\nApakah ingin melakukan scan lagi? (y/n): ")
        if scan_again.lower() != 'y':
            print(Fore.GREEN + "Terima kasih telah menggunakan Annie. Sampai jumpa!")
            break

if __name__ == "__main__":
    # Bersihkan layar terminal sebelum menjalankan skrip
    os.system('clear')
    run_nuclei()
