class Computer:
    def __init__(self, size, color, type):
        self.size = size
        self.color = color
        self.type = type

    def overview(self):
        print (f"Computer(size={self.size}, color={self.color}, type={self.type}")

computer1 = Computer("15 inches", "Silver", "Laptop")
computer2 = Computer("27 inches", "Black", "Desktop")

print(computer1)
print(computer2)
