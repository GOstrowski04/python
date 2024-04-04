class Account:
    def __init__(self, saldo_poczatkowe):
        self.saldo_poczatkowe = saldo_poczatkowe
        self.saldo_koncowe = saldo_poczatkowe

    def przelew_miedzy_kontami(self, other, kwota):
        if self.saldo_koncowe < kwota:
            print("Konto nie ma wystarczająco pieniędzy żeby wykonać przelew.")
            return
        other.saldo_koncowe += kwota
        self.saldo_koncowe -= kwota

    def przelew_zewnetrzny(self, x, kwota):
        if self.saldo_koncowe < kwota:
            print("Konto nie ma wystarczająco pieniędzy żeby wykonać przelew.")
            return
        x += kwota
        self.saldo_koncowe -= kwota

    def wplata(self, kwota):
        self.saldo_koncowe += kwota

    def wyplata(self, kwota):
        if self.saldo_koncowe < kwota:
            print("Konto nie ma wystarczająco pieniędzy żeby wypłacić pieniądze.")
            return
        self.saldo_koncowe -= kwota

    def __str__(self):
        return f"Saldo Początkowe: {self.saldo_poczatkowe}\nSaldo teraz: {self.saldo_koncowe}\n"


class PrivateAccount(Account):
    def __init__(self, saldo_poczatkowe):
        super().__init__(saldo_poczatkowe)

    def przelew_wynagrodzenia(self, kwota):
        self.saldo_koncowe += kwota


class FirmAccount(Account):
    def __init__(self, saldo_poczatkowe):
        super().__init__(saldo_poczatkowe)

    def przelew_do_zus(self, kwota):
        self.saldo_koncowe -= kwota

    def przelew_do_us(self, kwota):
        self.saldo_koncowe -= kwota


a1 = Account(2000)
a2 = Account(1500)
a3 = Account(4500)
print(a1)
print(a2)
print(a3)
bank = 0
a3.wplata(750)
a3.wyplata(300)
a1.przelew_miedzy_kontami(a2, 425)
a2.przelew_miedzy_kontami(a1, 900)
a3.przelew_zewnetrzny(bank, 2000)
print(a1)
print(a2)
print(a3)
