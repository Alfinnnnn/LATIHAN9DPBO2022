from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, luas_tanah, kapasitas_listrik):
        super().__init__("Indekos")
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.luas_tanah = luas_tanah
        self.kapasitas_listrik = kapasitas_listrik

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    def get_luas_tanah(self):
        return self.luas_tanah

    def get_kapasitas_listrik(self):
        return self.kapasitas_listrik

    def get_summary(self):
        return "Hunian Indekos."