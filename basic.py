def checkcats(CatsTuti, CatsNining):
    
    DeletedCats = CatsTuti.copy()
    del DeletedCats[1:3]  # Hapus indeks 2 dan 3
    
    
    corrected_tuti = CatsTuti.copy()
    del corrected_tuti[4]  # Hapus indeks 4
    del corrected_tuti[3]  # Hapus indeks 3 (setelah penghapusan indeks 4, indeks ini menjadi 3)
    del corrected_tuti[0]  # Hapus indeks 0 (setelah penghapusan indeks 3, indeks ini menjadi 0)
    
    # Buat array yang berisi data Tuti yang sudah dikoreksi
    corrected_tuti_array = [item for item in corrected_tuti if item is not None]
    
    # Buat array yang berisi data Tuti yang sudah dikoreksi dan data Nining
    combined_cats = corrected_tuti_array + CatsNining


    # Output hasil
    print("Data Anjing:", DeletedCats)
    print("Kucing Nining:", CatsNining)
    print("Data kucing tuti yang sudah dikoreksi + Data kuciing Nining:" ,combined_cats)
    

# Contoh penggunaan
CatsTuti = [3, 5, 12, 2, 7]
CatsNining = [4, 1, 15, 8, 3]

checkcats(CatsTuti, CatsNining)