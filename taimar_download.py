import time
import sys
import os
import random

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'

# ---------- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ----------

def slow_print(text, delay=0.02, color=GREEN):
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def scan_animation(lines=6, duration=1.2, color=GREEN, width=55):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*<>/\\|"
    for _ in range(lines):
        line = ''.join(random.choice(chars) for _ in range(width))
        sys.stdout.write(f"\r{color}{line}{RESET}")
        sys.stdout.flush()
        time.sleep(duration / lines)
    print()

def progress_bar(duration=3, color=GREEN, label=""):
    total = 100
    bar_length = 40
    for i in range(total + 1):
        percent = i / total
        filled_len = int(bar_length * percent)
        bar = '█' * filled_len + '-' * (bar_length - filled_len)
        sys.stdout.write(f'\r{label}{color}[{bar}]{RESET} {i}%')
        sys.stdout.flush()
        time.sleep(duration / total)
    print()

def loading_dots(text, duration=2, color=GREEN):
    sys.stdout.write(f"{color}{text}{RESET}")
    sys.stdout.flush()
    end = time.time() + duration
    while time.time() < end:
        for dot in [".", "..", "..."]:
            sys.stdout.write(f"\r{color}{text}{dot}{RESET}")
            sys.stdout.flush()
            time.sleep(0.3)
            if time.time() >= end:
                break
    print()

# ---------- АРТ ТАЙМАР ----------

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

# ---------- ЭТАПЫ ----------

def intro():
    os.system('clear')
    print(f"{CYAN}{BOLD}╔══════════════════════════════════════════════════╗")
    print("║         УСТАНОВЩИК СОФТА  «ТАЙМАР»              ║")
    print("║                  версия 3.1                     ║")
    print("╚══════════════════════════════════════════════════╝" + f"{RESET}")
    print()
    time.sleep(0.8)
    slow_print("[*] Подготовка к установке...", 0.02, CYAN)
    time.sleep(0.5)
    slow_print("[*] Проверка прав доступа...", 0.02, CYAN)
    progress_bar(1.5, CYAN, "[*] ")
    print()
    slow_print("[+] Права получены.", 0.02, GREEN)
    time.sleep(0.5)

def cable_check():
    os.system('clear')
    print(f"{YELLOW}{BOLD}=== ПОДКЛЮЧЕНИЕ УСТРОЙСТВА ==={RESET}")
    print()
    time.sleep(0.5)
    slow_print("[*] Подключите устройство кабелем к системе...", 0.03, YELLOW)
    time.sleep(0.8)
    loading_dots("[*] Ожидание подключения", 2, YELLOW)
    time.sleep(0.3)
    scan_animation(4, 1.0, CYAN, 55)
    print()
    slow_print("[+] Устройство обнаружено.", 0.02, GREEN)
    time.sleep(0.3)
    slow_print("[*] Идентификация...", 0.02, CYAN)
    time.sleep(0.5)
    scan_animation(3, 0.8, MAGENTA, 55)
    print()
    slow_print("[+] Устройство идентифицировано.", 0.02, GREEN)
    time.sleep(0.5)

def wait_permission():
    os.system('clear')
    print(f"{YELLOW}{BOLD}=== ЗАПРОС РАЗРЕШЕНИЯ ==={RESET}")
    print()
    time.sleep(0.5)
    print(f"{CYAN}╔══════════════════════════════════════════════════╗")
    print("║   Система запрашивает разрешение на установку    ║")
    print("║              софта «ТАЙМАР».                     ║")
    print("║                                                  ║")
    print("║   Разрешить установку? (y/n)                     ║")
    print("╚══════════════════════════════════════════════════╝" + f"{RESET}")
    print()

    while True:
        answer = input(f"{GREEN}Ваш ответ: {RESET}").strip().lower()
        if answer == 'y':
            print()
            slow_print("[+] Разрешение получено.", 0.02, GREEN)
            time.sleep(0.5)
            break
        elif answer == 'n':
            print()
            slow_print("[!] Установка отменена пользователем.", 0.02, RED)
            time.sleep(1)
            sys.exit(0)
        else:
            print(f"{YELLOW}[!] Введите 'y' или 'n'.{RESET}")

def installation():
    os.system('clear')
    print(f"{CYAN}{BOLD}=== УСТАНОВКА СОФТА «ТАЙМАР» ==={RESET}")
    print()
    time.sleep(0.5)

    steps = [
        ("Распаковка архива", 3),
        ("Установка ядра", 3),
        ("Настройка модулей", 2.5),
        ("Подключение к сети ТАЙМАР", 3),
        ("Синхронизация данных", 2.5),
        ("Финальная настройка", 2)
    ]

    for step, dur in steps:
        sys.stdout.write(f"\r{CYAN}[*] {step}...{RESET}")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(f"\r{GREEN}[+] {step}... OK{RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
        print()
        progress_bar(dur, GREEN, "    ")
        print()

    slow_print("[+] Все компоненты установлены.", 0.02, GREEN)
    time.sleep(0.5)

def finalization():
    os.system('clear')
    print(f"{YELLOW}{BOLD}=== ЗАВЕРШЕНИЕ УСТАНОВКИ ==={RESET}")
    print()
    time.sleep(0.5)
    loading_dots("[*] Регистрация в системе", 2, CYAN)
    time.sleep(0.3)
    loading_dots("[*] Применение настроек", 2, CYAN)
    time.sleep(0.3)
    loading_dots("[*] Проверка целостности", 2, CYAN)
    time.sleep(0.5)
    print()
    slow_print("[+] Установка завершена.", 0.03, GREEN)
    time.sleep(0.8)

def welcome():
    os.system('clear')
    time.sleep(0.5)
    print(taimar_art)
    time.sleep(1)
    slow_print(f"{GREEN}{BOLD}СОФТ УСТАНОВЛЕН.{RESET}", 0.05, GREEN)
    time.sleep(0.5)
    slow_print(f"{GREEN}Добро пожаловать в ТАЙМАР.{RESET}", 0.06, GREEN)
    time.sleep(0.5)
    print()
    slow_print(f"{RED}Теперь ты с нами.{RESET}", 0.08, RED)
    time.sleep(1)
    print()
    slow_print(f"{YELLOW}[*] Запустить ТАЙМАР? Введи команду: taimar{RESET}", 0.02, YELLOW)
    print()

# ---------- ЗАПУСК ----------

if __name__ == "__main__":
    os.system('clear')
    intro()
    cable_check()
    wait_permission()
    installation()
    finalization()
    welcome()
