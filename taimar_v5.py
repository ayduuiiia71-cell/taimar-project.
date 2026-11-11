import time
import sys
import os
import random

# ---------- ЦВЕТА ----------
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
WHITE = '\033[97m'
BLUE = '\033[94m'
GREY = '\033[90m'
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'

# ---------- БАЗОВЫЕ ФУНКЦИИ ----------
def tstamp():
    return time.strftime("%H:%M:%S")

def log(text, color=GREEN, prefix="[*]", delay=0.3, pause=True):
    line = f"{GREY}[{tstamp()}]{RESET} {color}{prefix}{RESET} {text}"
    print(line)
    sys.stdout.flush()
    if pause:
        time.sleep(delay)

def log_ok(text, delay=0.3): log(text, GREEN, "[OK]", delay)
def log_info(text, delay=0.3): log(text, CYAN, "[*]", delay)
def log_warn(text, delay=0.4): log(text, YELLOW, "[!]", delay)
def log_fail(text, delay=0.4): log(text, RED, "[X]", delay)

def log_proc(text, delay=0.25):
    sys.stdout.write(f"{GREY}[{tstamp()}]{RESET} {CYAN}[*]{RESET} {text}")
    sys.stdout.flush()
    for _ in range(3):
        time.sleep(delay)
        sys.stdout.write(".")
        sys.stdout.flush()
    time.sleep(delay)
    print(f" {GREEN}OK{RESET}")
    sys.stdout.flush()

def banner(title, color=CYAN):
    w = 60
    print(f"{color}{BOLD}╔" + "═" * w + "╗")
    print("║" + title.center(w) + "║")
    print("╚" + "═" * w + "╝" + f"{RESET}")
    print()

def separator(color=GREY):
    print(f"{color}" + "─" * 62 + f"{RESET}")

def ask_yes_no(prompt, color=YELLOW):
    while True:
        answer = input(f"{color}{prompt} (y/n): {RESET}").strip().lower()
        if answer == 'y': return True
        elif answer == 'n': return False
        else: print(f"{YELLOW}[!] Введите 'y' или 'n'.{RESET}")

def progress_bar(duration=3, color=GREEN, label="", width=40):
    total = 100
    for i in range(total + 1):
        percent = i / total
        filled = int(width * percent)
        bar = '█' * filled + '░' * (width - filled)
        sys.stdout.write(f'\r{label}{color}[{bar}]{RESET} {i:3d}%')
        sys.stdout.flush()
        time.sleep(duration / total)
    print()

def typing(text, color=CYAN, delay=0.02):
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def random_delay(a=0.2, b=1.2):
    time.sleep(random.uniform(a, b))

# ---------- АРТ ----------
taimar_art = f"""
{RED}{BOLD}
████████╗ █████╗ ██╗   ██╗███╗   ███╗ █████╗ ██████╗
╚══██╔══╝██╔══██╗╚██╗ ██╔╝████╗ ████║██╔══██╗██╔══██╗
   ██║   ███████║ ╚████╔╝ ██╔████╔██║███████║██████╔╝
   ██║   ██╔══██║  ╚██╔╝  ██║╚██╔╝██║██╔══██║██╔══██╗
   ██║   ██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║  ██║
   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
{RESET}
"""

# ---------- МЕНЮ ----------
def show_menu():
    os.system('clear')
    print(f"{RED}{BOLD}╔" + "═" * 60 + "╗")
    print("║" + "  ТАЙМАР — ЦЕНТР УПРАВЛЕНИЯ  v3.5  ".center(60) + "║")
    print("╚" + "═" * 60 + "╝" + f"{RESET}")
    print()
    print(f"  {GREY}Статус:{RESET}     {GREEN}● АКТИВНА{RESET}")
    print(f"  {GREY}Оператор:{RESET}   {CYAN}АНОНИМ{RESET}")
    print(f"  {GREY}Время:{RESET}      {WHITE}{tstamp()}{RESET}")
    print(f"  {GREY}Сеть:{RESET}       {GREEN}СТАБИЛЬНА{RESET}")
    print()
    separator()
    print(f"{CYAN}{BOLD}  ДОСТУПНЫЕ ФУНКЦИИ{RESET}")
    separator()
    print()
    print(f"  {GREEN}[1]{RESET}  Атака на сервера МОНОЛИТ")
    print(f"  {GREEN}[2]{RESET}  Проверка серверов ТАЙМАР на проникновение")
    print(f"  {GREEN}[3]{RESET}  Проверка антенны в главном штабе")
    print(f"  {GREEN}[4]{RESET}  Проверка бортового компьютера в главном штабе")
    print(f"  {MAGENTA}[5]{RESET}  Скрытый терминал (Опасно)")
    print()
    print(f"  {RED}[0]{RESET}  Выход")
    print()
    separator()

def main_menu():
    while True:
        show_menu()
        choice = input(f"{YELLOW}  > {RESET}").strip()
        if choice == '1': attack_monolit()
        elif choice == '2': check_servers()
        elif choice == '3': check_antenna()
        elif choice == '4': check_onboard_computer()
        elif choice == '5': hidden_terminal()
        elif choice == '0':
            log_info("Завершение сессии...")
            time.sleep(1)
            break
        else:
            log_fail("Неверный выбор")
            time.sleep(1)

# ---------- ФУНКЦИЯ 1: АТАКА НА МОНОЛИТ ----------
def attack_monolit():
    os.system('clear')
    banner("ФУНКЦИЯ 1: АТАКА НА СЕРВЕРА МОНОЛИТ", RED)
    time.sleep(0.5)
    log_info("Подготовка к операции...")
    log_info("Цель: враждебная группировка МОНОЛИТ")
    log_warn("Уровень риска: ВЫСОКИЙ")
    print()

    if not ask_yes_no(f"{RED}Подтвердите запуск атаки на МОНОЛИТ?{RESET}"):
        log_warn("Атака отменена.")
        time.sleep(1.5)
        return

    while True:
        success = run_attack()
        if success: break
        print()
        if not ask_yes_no(f"{RED}Повторить атаку?{RESET}"):
            log_warn("Атака отменена.")
            time.sleep(1.5)
            return
    print()
    log_info("Возврат в меню...")
    time.sleep(1.5)

def run_attack():
    os.system('clear')
    banner("АТАКА НА МОНОЛИТ — НАЧАЛО", RED)
    duration_min = random.choice([2, 2, 3, 3, 4, 5, 7, 10])
    log_info(f"Расчётное время операции: ~{duration_min} мин.")
    print()

    log_proc("Инициализация боевого модуля")
    log_proc("Загрузка сигнатур")
    log_ok("Канал связи стабилен")
    print()

    log_info("Разведка сети МОНОЛИТ...")
    for ip in ["10.0.0.1", "10.0.0.14", "10.0.0.27", "10.0.0.55"]:
        log_ok(f"Найден узел: {ip}", 0.4)
    print()

    log_info("Подбор пароля к узлу monolit-core.dark...")
    for pwd in ["admin", "123456", "monolit", "root", "toor", "matrix"]:
        time.sleep(random.uniform(0.2, 0.5))
        if random.random() < 0.1:
            log_ok(f"Пароль найден: {pwd}"); break
        log_fail(f"Попытка '{pwd}' — FAILED", 0.05)
    print()

    log_info("Обход файрвола...")
    log_proc("Обход: Сетевой фильтр")
    log_proc("Обход: DPI-анализ")
    log_ok("Файрвол обойдён")
    print()

    log_info("Загрузка полезной нагрузки...")
    progress_bar(4, MAGENTA, "    ")
    log_ok("Нагрузка доставлена")
    print()

    log_info("Взлом узлов МОНОЛИТ...")
    for node in ["node-01", "node-02", "core"]:
        log_proc(f"Взлом: monolit-{node}.dark")
    log_ok("Ядро МОНОЛИТ взломано")
    print()

    log_warn("Активация протокола 'Чистый лист'...")
    for i in range(3, 0, -1):
        sys.stdout.write(f"\r{GREY}[{tstamp()}]{RESET} {RED}[!]{RESET} Уничтожение через {i}...")
        sys.stdout.flush()
        time.sleep(1)
    print()
    log_ok("Сервера МОНОЛИТ уничтожены")
    print()

    if random.random() < 0.3:
        log_fail("КРИТИЧЕСКАЯ ОШИБКА: обратный трек")
        log_fail("АТАКА ПРОВАЛЕНА")
        time.sleep(1)
        return False
    else:
        log_ok("Все узлы скомпрометированы")
        print(f"{RED}{BOLD}  [X] СЕРВЕРА МОНОЛИТ УНИЧТОЖЕНЫ.{RESET}")
        time.sleep(1)
        return True

# ---------- ФУНКЦИЯ 2: ПРОВЕРКА СЕРВЕРОВ ----------
def check_servers():
    os.system('clear')
    banner("ФУНКЦИЯ 2: ПРОВЕРКА СЕРВЕРОВ ТАЙМАР", YELLOW)
    time.sleep(0.5)
    log_info("Запуск глубокого сканирования...")
    print()

    checks = ["Брандмауэр", "Порты", "Целостность данных", "Сетевой трафик", "Базы данных", "Логи", "Учётные записи"]
    for i, name in enumerate(checks, 1):
        sys.stdout.write(f"\r{CYAN}[{i}/{len(checks)}]{RESET} Проверка: {name}...")
        sys.stdout.flush()
        time.sleep(random.uniform(0.5, 1.2))
        print(f" {GREEN}OK{RESET}")
        log_ok("Подсистема в норме", 0.1)
    print()

    separator()
    if random.random() < 0.2:
        log_fail("ВНИМАНИЕ: ОБНАРУЖЕНА УГРОЗА")
        if ask_yes_no(f"{RED}Предотвратить угрозу?{RESET}"):
            progress_bar(3, GREEN, "    ")
            log_ok("Угроза предотвращена")
        else:
            log_warn("Угроза не предотвращена.")
    else:
        log_ok("Угроз не обнаружено")
        log_ok("Система в безопасности")
    print()
    log_info("Возврат в меню...")
    time.sleep(1.5)

# ---------- ФУНКЦИЯ 3: ПРОВЕРКА АНТЕННЫ ----------
def check_antenna():
    os.system('clear')
    banner("ФУНКЦИЯ 3: ПРОВЕРКА АНТЕННЫ", YELLOW)
    time.sleep(0.5)
    log_info("Сканирование антенного модуля...")
    print()

    checks = ["Питание", "Сигнал", "Частоты", "Соединение", "Направленность", "Кабель"]
    for i, name in enumerate(checks, 1):
        sys.stdout.write(f"\r{CYAN}[{i}/{len(checks)}]{RESET} Проверка: {name}...")
        sys.stdout.flush()
        time.sleep(random.uniform(0.5, 1.2))
        print(f" {GREEN}OK{RESET}")
        log_ok("Параметр в норме", 0.1)
    print()

    separator()
    if random.random() < 0.25:
        log_fail("ОБНАРУЖЕНА ПРОБЛЕМА С АНТЕННОЙ")
        log_warn("Подсоедините кабель к антенне")
        if ask_yes_no(f"{YELLOW}Начать восстановление?{RESET}"):
            log_proc("Поиск устройства")
            progress_bar(3, GREEN, "    ")
            log_ok("Сигнал восстановлен")
        else:
            log_warn("Восстановление отменено.")
    else:
        log_ok("Антенна в штатном режиме")
    print()
    log_info("Возврат в меню...")
    time.sleep(1.5)

# ---------- ФУНКЦИЯ 4: БОРТОВОЙ КОМПЬЮТЕР ----------
def check_onboard_computer():
    os.system('clear')
    banner("ФУНКЦИЯ 4: ПРОВЕРКА БОРТОВОГО КОМПЬЮТЕРА", YELLOW)
    time.sleep(0.5)
    log_info("Сканирование бортового компьютера...")
    print()

    checks = ["Процессор", "Память", "Накопители", "Питание", "Охлаждение", "Сеть", "ПО"]
    for i, name in enumerate(checks, 1):
        sys.stdout.write(f"\r{CYAN}[{i}/{len(checks)}]{RESET} Проверка: {name}...")
        sys.stdout.flush()
        time.sleep(random.uniform(0.5, 1.2))
        print(f" {GREEN}OK{RESET}")
        log_ok("Система в норме", 0.1)
    print()

    separator()
    if random.random() < 0.25:
        log_fail("ОБНАРУЖЕНА ПРОБЛЕМА С БОРТОВЫМ КОМПЬЮТЕРОМ")
        log_warn("Подсоедините кабель к бортовому компьютеру")
        if ask_yes_no(f"{YELLOW}Восстановить сигнал и доступ?{RESET}"):
            log_proc("Поиск устройства")
            progress_bar(2, GREEN, "    ")
            log_ok("Сигнал восстановлен")
            progress_bar(2, GREEN, "    ")
            log_ok("Доступ восстановлен")
        else:
            log_warn("Восстановление отменено.")
    else:
        log_ok("Бортовой компьютер в штатном режиме")
    print()
    log_info("Возврат в меню...")
    time.sleep(1.5)

# ---------- ФУНКЦИЯ 5: СКРЫТЫЙ ТЕРМИНАЛ ----------
def hidden_terminal():
    os.system('clear')
    banner("СКРЫТЫЙ ТЕРМИНАЛ ТАЙМАР", MAGENTA)
    time.sleep(0.5)
    log_info("Инициализация защищённого канала...")
    time.sleep(0.5)
    log_proc("Обход шлюза")
    log_ok("Доступ к скрытой консоли получен.")
    print()
    print(f"{GREY}Введите 'help' для списка команд.{RESET}")
    print()

    while True:
        try:
            cmd_input = input(f"{MAGENTA}TaimarNet > {RESET}").strip().lower()
            if not cmd_input: continue
            parts = cmd_input.split()
            command = parts[0]
            target = parts[1] if len(parts) > 1 else None

            if command == 'help':
                print(f"\n{CYAN}Доступные команды:{RESET}")
                print(f"  {GREEN}help{RESET}           - Показать этот список")
                print(f"  {GREEN}scan <цель>{RESET}    - Сканировать сеть (например: scan monolit)")
                print(f"  {GREEN}hack <цель>{RESET}    - Начать атаку на узел (например: hack monolit-core)")
                print(f"  {GREEN}status{RESET}         - Показать статус системы")
                print(f"  {GREEN}clear{RESET}          - Очистить экран")
                print(f"  {GREEN}exit{RESET}           - Вернуться в главное меню\n")

            elif command == 'clear': os.system('clear')

            elif command == 'status':
                print()
                log_ok("Система: ТАЙМАР v3.5")
                log_ok("Статус ядра: СТАБИЛЕН")
                log_warn("Уровень тревоги: НИЗКИЙ")
                print()

            elif command == 'scan':
                if not target:
                    log_fail("Укажите цель. Пример: scan monolit")
                    continue
                print()
                log_info(f"Запуск сканирования: {target}...")
                for i in range(1, random.randint(3, 6)):
                    time.sleep(random.uniform(0.3, 0.8))
                    log_ok(f"Найден узел: 10.0.{random.randint(0,255)}.{random.randint(1,254)} (порт открыт)")
                log_ok("Сканирование завершено.\n")

            elif command == 'hack':
                if not target:
                    log_fail("Укажите цель. Пример: hack monolit-core")
                    continue
                print()
                log_warn(f"Атака на узел: {target}")
                log_proc("Обход защиты")
                progress_bar(2, RED, "    ")
                if random.random() < 0.3:
                    log_fail(f"АТАКА НА {target.upper()} ПРОВАЛЕНА.")
                else:
                    log_ok(f"УЗЕЛ {target.upper()} ВЗЛОМАН. Данные скопированы.\n")

            elif command == 'exit':
                log_info("Отключение...")
                time.sleep(1)
                break

            elif command == 'taimar_override':
                print()
                log_warn("АКТИВИРОВАН ПРОТОКОЛ ПЕРЕЗАГРУЗКИ")
                log_fail("ПЕРЕДАЧА ДАННЫХ ШТАБУ...")
                time.sleep(1)
                log_ok("Вы — избранный. ТАЙМАР гордится вами.\n")

            else:
                log_fail(f"Неизвестная команда: '{command}'. Введите 'help'.\n")

        except KeyboardInterrupt:
            print("\n")
            log_warn("Прерывание. Выход в меню.")
            break

# ---------- ЗАПУСК ----------
def main():
    os.system('clear')
    print(f"{CYAN}{BOLD}╔" + "═" * 60 + "╗")
    print("║" + "  СИСТЕМА УПРАВЛЕНИЯ «ТАЙМАР» v3.5  ".center(60) + "║")
    print("╚" + "═" * 60 + "╝" + f"{RESET}")
    print()
    time.sleep(0.5)
    log_info("Ожидание команды 'start'...")
    print()

    while True:
        cmd = input(f"{YELLOW}  > {RESET}").strip().lower()
        if cmd == 'start': break
        else: log_fail("Неизвестная команда. Введите 'start'.")

    os.system('clear')
    time.sleep(0.5)
    print(taimar_art)
    time.sleep(1.5)
    log_ok("Центр управления ТАЙМАР запущен")
    time.sleep(1)
    main_menu()
    log_info("Сессия завершена.")

if __name__ == "__main__":
    main()
