# ===================================
# [Sistem Administrasi Perpustakaan]
# ===================================
# Developed by. Fakhri Maulana Herza
# JCDS - [0512]

# /===== Data Model =====/

from datetime import datetime, timedelta
import os
import csv

books = {
    1: {"title": "Python for Beginners", "status": "tersedia"},
    2: {"title": "Machine Learning Basics", "status": "tersedia"},
    3: {"title": "Deep Learning with Python", "status": "tersedia"},
    4: {"title": "Data Science Handbook", "status": "tersedia"},
    5: {"title": "Artificial Intelligence", "status": "tersedia"},
    6: {"title": "Big Data Analytics", "status": "tersedia"},
    7: {"title": "Cloud Computing Essentials", "status": "tersedia"},
    8: {"title": "Cyber Security Principles", "status": "tersedia"},
    9: {"title": "Blockchain Basics", "status": "tersedia"},
    10: {"title": "Internet of Things (IoT)", "status": "tersedia"},
    11: {"title": "Computer Vision", "status": "tersedia"},
    12: {"title": "Natural Language Processing", "status": "tersedia"},
    13: {"title": "Software Engineering", "status": "tersedia"},
    14: {"title": "Database Management", "status": "tersedia"},
    15: {"title": "Operating Systems", "status": "tersedia"},
    16: {"title": "Networking Fundamentals", "status": "tersedia"},
    17: {"title": "Quantum Computing", "status": "tersedia"},
    18: {"title": "Ethical Hacking", "status": "tersedia"},
    19: {"title": "Robotics Engineering", "status": "tersedia"},
    20: {"title": "Programming in C++", "status": "tersedia"}
}

transactions = [
    {"book_id": 1, "nik": "1234567890", "name": "Ali", "borrow_date": datetime.now() - timedelta(days=5), "return_date": None, "notes": "", "extension_count": 0},
    {"book_id": 2, "nik": "0987654321", "name": "Budi", "borrow_date": datetime.now() - timedelta(days=3), "return_date": datetime.now(), "notes": "Bagus", "extension_count": 1},
    {"book_id": 3, "nik": "1122334455", "name": "Citra", "borrow_date": datetime.now() - timedelta(days=2), "return_date": None, "notes": "", "extension_count": 0},
    {"book_id": 4, "nik": "2233445566", "name": "Dedi", "borrow_date": datetime.now() - timedelta(days=6), "return_date": None, "notes": "", "extension_count": 1},
    {"book_id": 5, "nik": "3344556677", "name": "Eka", "borrow_date": datetime.now() - timedelta(days=1), "return_date": None, "notes": "", "extension_count": 0},
    {"book_id": 6, "nik": "4455667788", "name": "Farhan", "borrow_date": datetime.now() - timedelta(days=7), "return_date": datetime.now(), "notes": "Kondisi baik", "extension_count": 0},
    {"book_id": 7, "nik": "5566778899", "name": "Gina", "borrow_date": datetime.now() - timedelta(days=4), "return_date": None, "notes": "", "extension_count": 0},
    {"book_id": 8, "nik": "6677889900", "name": "Hadi", "borrow_date": datetime.now() - timedelta(days=5), "return_date": None, "notes": "", "extension_count": 1},
    {"book_id": 9, "nik": "7788990011", "name": "Indah", "borrow_date": datetime.now() - timedelta(days=3), "return_date": None, "notes": "", "extension_count": 0},
    {"book_id": 10, "nik": "8899001122", "name": "Joko", "borrow_date": datetime.now() - timedelta(days=8), "return_date": datetime.now(), "notes": "Sampul agak rusak", "extension_count": 1}
]

admin_credentials = {"admin": "password123"}

# /===== Feature Program =====/

def authenticate():
    username = input("Masukkan username admin: ")
    password = input("Masukkan password: ")
    return admin_credentials.get(username) == password

def add_book(title):
    # Periksa apakah judul sudah ada di dalam koleksi buku
    for book in books.values():
        if book["title"].lower() == title.lower():
            print("Buku sudah ada dalam koleksi.")
            return
    # Tambahkan buku jika tidak duplikat
    book_id = len(books) + 1
    books[book_id] = {"title": title, "status": "tersedia"}
    print("Buku berhasil ditambahkan.")

def list_books():
    print("\nDaftar Buku:")
    for book_id, book in books.items():
        print(f"ID: {book_id}, Judul: {book['title']}, Status: {book['status']}")

def has_borrowed(nik):
    for transaction in transactions:
        if transaction["nik"] == nik and transaction["return_date"] is None:
            return True
    return False

def borrow_book(book_id, nik, name):
    if has_borrowed(nik):
        print("Anda hanya dapat meminjam satu buku. Kembalikan buku sebelumnya terlebih dahulu.")
        return
    
    if book_id in books and books[book_id]["status"] == "tersedia":
        books[book_id]["status"] = "tidak"
        borrow_date = datetime.now()
        transactions.append({
            "book_id": book_id,
            "nik": nik,
            "name": name,
            "borrow_date": borrow_date,
            "return_date": None,
            "notes": "",
            "extension_count": 0
        })
        print("Buku berhasil dipinjam.")
    else:
        print("Buku tidak tersedia atau ID tidak valid.")

def return_book(book_id, notes=""):
    for transaction in transactions:
        if transaction["book_id"] == book_id and transaction["return_date"] is None:
            transaction["return_date"] = datetime.now()
            transaction["notes"] = notes
            books[book_id]["status"] = "tersedia"
            print("Buku berhasil dikembalikan.")
            return
    print("Buku ini tidak sedang dipinjam atau ID tidak valid.")

def extend_loan(nik):
    for transaction in transactions:
        if transaction["nik"] == nik and transaction["return_date"] is None:
            if transaction["extension_count"] < 1:
                transaction["borrow_date"] += timedelta(days=3)
                transaction["extension_count"] += 1
                print("Peminjaman berhasil diperpanjang 3 hari.")
            else:
                print("Anda sudah melakukan perpanjangan sebelumnya. Tidak dapat diperpanjang lagi.")
            return
    print("Tidak ada buku yang sedang dipinjam oleh NIK ini.")

def transaction_history():
    print("\nRiwayat Peminjaman:")
    for trans in transactions:
        borrow_date_str = trans["borrow_date"].strftime("%Y-%m-%d %H:%M:%S")
        return_date_str = trans["return_date"].strftime("%Y-%m-%d %H:%M:%S") if trans["return_date"] else "Belum dikembalikan"
        print(f"ID Buku: {trans['book_id']}, NIK: {trans['nik']}, Nama: {trans['name']}, "
              f"Tanggal Pinjam: {borrow_date_str}, Tanggal Kembali: {return_date_str}, "
              f"Catatan: {trans['notes']}, Perpanjangan: {trans['extension_count']}")

def search_data():
    search_key = input("Masukkan ID Buku atau Nama Peminjam: ")
    print("\nHasil Pencarian:")
    for book_id, book in books.items():
        if str(book_id) == search_key or any(trans["name"].lower() == search_key.lower() for trans in transactions if trans["book_id"] == book_id):
            print(f"ID: {book_id}, Judul: {book['title']}, Status: {book['status']}")

def delete_history():
    if not authenticate():
        print("Autentikasi gagal! Tidak dapat menghapus riwayat.")
        return
    
    if not os.path.exists("recycle_bin"):
        os.makedirs("recycle_bin")
    
    file_path = os.path.join("recycle_bin", "deleted_history.csv")
    
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID Buku", "NIK", "Nama", "Tanggal Pinjam", "Tanggal Kembali", "Catatan", "Perpanjangan"])
        for trans in transactions:
            writer.writerow([trans["book_id"], trans["nik"], trans["name"], trans["borrow_date"], trans["return_date"], trans["notes"], trans["extension_count"]])
    
    transactions.clear()
    print("Riwayat berhasil dihapus dan disimpan di recycle_bin/deleted_history.csv")

# /===== Main Program =====/

def main_menu():
    if not authenticate():
        print("Login gagal! Program keluar.")
        return
    
    while True:
        print("\n=== Sistem Peminjaman Buku ===")
        print("1. Tambah Buku")
        print("2. Lihat Daftar Buku")
        print("3. Pinjam Buku")
        print("4. Kembalikan Buku")
        print("5. Perpanjang Peminjaman")
        print("6. Lihat Riwayat Peminjaman")
        print("7. Cari Data Buku atau Peminjam")
        print("8. Hapus Riwayat Peminjaman")
        print("9. Keluar")
        
        choice = input("Pilih menu: ")
        
        if choice == "1":
            title = input("Masukkan judul buku: ")
            add_book(title)
        elif choice == "2":
            list_books()
        elif choice == "3":
            book_id = int(input("Masukkan ID buku: "))
            nik = input("Masukkan NIK: ")
            name = input("Masukkan Nama: ")
            borrow_book(book_id, nik, name)
        elif choice == "4":
            book_id = int(input("Masukkan ID buku: "))
            notes = input("Masukkan catatan pengembalian: ")
            return_book(book_id, notes)
        elif choice == "5":
            nik = input("Masukkan NIK: ")
            extend_loan(nik)
        elif choice == "6":
            transaction_history()
        elif choice == "7":
            search_data()
        elif choice == "8":
            delete_history()
        elif choice == "9":
            print("Terima kasih telah menggunakan sistem ini!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main_menu()