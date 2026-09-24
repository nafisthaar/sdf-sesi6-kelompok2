# CLEAN CODE
def hitung_biaya_parkir(lama_parkir_jam, is_member):
    TARIF_PER_JAM = 3000
    DISKON_MEMBER = 0.15
    
    total_biaya = lama_parkir_jam * TARIF_PER_JAM
    
    if is_member == 1:
        potongan_biaya = total_biaya * DISKON_MEMBER
        total_biaya -= potongan_biaya
        
    print(f"Biaya parkir: {total_biaya}")

hitung_biaya_parkir(4, 1)