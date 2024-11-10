#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: RPL 1A
#Kelompok: 8 ~ KNOPPIX

class RiverCrossing:
    def __init__(self):
        self.sisi_awal = ["S1", "I1", "S2", "I2", "S3", "I3"]
        self.sisi_seberang = []
        self.boat = []

    def move(self, from_side, to_side, person1, person2=None):
        from_side.remove(person1)
        to_side.append(person1)
        if person2:
            from_side.remove(person2)
            to_side.append(person2)
        self.boat = [person1] if not person2 else [person1, person2]
        print(f"{person1} {'dan ' + person2 if person2 else ''} menyeberang.")

    def check_position(self):
        print(f"Sisi Awal: {self.sisi_awal}")
        print(f"Sisi Seberang: {self.sisi_seberang}")
        print("----")

    def is_crossing_complete(self):
        return not self.sisi_awal

    def solve(self):
        self.check_position()
        self.move(self.sisi_awal, self.sisi_seberang, "S1", "S2")  
        self.check_position()
        
        self.move(self.sisi_seberang, self.sisi_awal, "S2")         
        self.check_position()
        
        self.move(self.sisi_awal, self.sisi_seberang, "S2", "S3")   
        self.check_position()
        
        self.move(self.sisi_seberang, self.sisi_awal, "S3")         
        self.check_position()
        
        self.move(self.sisi_awal, self.sisi_seberang, "I3", "S3")   
        self.check_position()
        
        self.move(self.sisi_seberang, self.sisi_awal, "I3")         
        self.check_position()
        
        self.move(self.sisi_awal, self.sisi_seberang, "I2", "I3")   
        self.check_position()
        
        self.move(self.sisi_seberang, self.sisi_awal, "I2")        
        self.check_position()
        
        self.move(self.sisi_awal, self.sisi_seberang, "I1", "I2")   
        self.check_position()

        if self.is_crossing_complete():
            print("Semua pasangan berhasil menyeberang!")
        else:
            print("Tidak semua pasangan berhasil menyeberang.")

if __name__ == "__main__":
    crossing = RiverCrossing()
    crossing.solve()
