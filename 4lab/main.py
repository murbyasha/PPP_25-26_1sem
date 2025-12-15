rates = {"RUB": 1.0}
base = "RUB"

class Money:
    def __init__(self, amount, currency):
        self.amount = float(amount)
        self.currency = currency
    
    def base_value(self):
        return self.amount * rates.get(self.currency, 0)
    
    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"
    
    def full_str(self):
        return f"{self.amount:.2f} {self.currency} = {self.base_value():.2f} {base}"
    
    def __lt__(self, other):
        return self.base_value() < other.base_value()

#парсинг разных форматов
def parse_code(s):
    try:
        if s.startswith("code "):
            parts = s[5:].split()
            return Money(parts[0], parts[1])
    except:
        pass
    return None

def parse_json(s):
    try:
        if s.startswith("json "):
            s = s[5:].replace("'", '"')
            d = eval(s)
            return Money(d["amount"], d["currency"])
    except:
        pass
    return None

def parse_local(s):
    try:
        if s.startswith("local "):
            s = s[6:]
            currency_map = {'₽': 'RUB', '$': 'USD', '€': 'EUR', '¥': 'CNY'}
            symbol = s[-1]
            num = s[:-1].replace(' ', '').replace(',', '.')
            return Money(num, currency_map.get(symbol, symbol))
    except:
        pass
    return None

def parse_default(s):
    try:
        if s.startswith("default "):
            return Money(s[8:], base)
    except:
        pass
    return None

#парсинг входных данных
def setup():
    global base, rates
    
    #базовая валюту
    base = input("базовая валюта: ").strip()
    rates = {base: 1.0}
    
    #курсы валют
    while True:
        line = input().strip()
        if not line:
            break
        cur, rate = line.split()
        rates[cur] = float(rate)

def main():
    setup()
    amounts = []
    parsers = [parse_code, parse_json, parse_local, parse_default]
    
    while True:
        try:
            line = input().strip()
            if not line:
                break
        except:
            break
        
        money = None
        for parser in parsers:
            money = parser(line)
            if money:
                break
        
        if money:
            if money.currency in rates:
                amounts.append(money)
            else:
                print(f"Ошибка: неизвестная валюта '{money.currency}' в '{line}'")
        else:
            print(f"Ошибка: неверный формат '{line}'")
    
    cmd = input().strip()
    
    if cmd == "sum":
        total = sum(m.base_value() for m in amounts)
        print(f"Total: {total:.2f} {base}")
    
    elif cmd in ["max", "min"]:
        if amounts:
            money = max(amounts) if cmd == "max" else min(amounts)
            print(f"{cmd.capitalize()}: {money.full_str()}")
        else:
            print("Нет данных")
    
    elif cmd == "list":
        for money in amounts:
            print(money.full_str())
    
    elif cmd == "sort":
        for money in sorted(amounts):
            print(money.full_str())

main()
