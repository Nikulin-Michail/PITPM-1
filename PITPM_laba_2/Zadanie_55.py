class Text:
    def __init__(self, text):
        self.text = text

    def kolich_simvol(self):
        return len(self.text)

    def kolich_bykv(self):
        return sum(1 for char in self.text if char.isalpha())

    def kolich_probelov(self):
        return sum(1 for char in self.text if char.isspace())

    def kolich_simvol_bez_probelov(self):
        return len(self.text.replace(" ", ""))

    def mass_slov(self):
        return self.text.split()

    def mass_predloz(self):
        return self.text.split(".!?")

text = Text("Это пример текста. Здесь есть несколько предложений. И некоторые слова.")

print(text.kolich_simvol())
print(text.kolich_bykv())
print(text.kolich_probelov())
print(text.kolich_simvol_bez_probelov())
print(text.mass_slov())
print(text.mass_predloz())