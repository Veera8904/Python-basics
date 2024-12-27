class bench:
    def __init__(self, color, bench, size):
        self.color = color  
        self.bench_type = bench
        self.size = size

    def overview(self):
        print(f"{self.size} {self.bench_type} bench\nColor : {self.color}\n")



mybench1 = bench("red", "steel", "Small")
mybench1.color = "White"

mybench2 =bench("Red", "wood", "Large")


mybench1.overview()
mybench2.overview()