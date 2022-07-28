from typing import NamedTuple

list_of_log = [
    "May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated",
    "May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.",
    "May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...",
    "May 20 11:01:12 PC-00102 PackageKit: daemon start",
    "May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...",
    "May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00",
    'May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"',
    "May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device",
    "May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio",
    "May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.",
    "May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.",
]


class Log_categories(NamedTuple):
    '''
    Кортеж разбитый по категориям, для хранения лога.
    '''
    time: str #Лучше хранить этот тип в datatime, но в задании этого нет
    pc_name: str
    service_name: str
    message: str


class Sub_categories(NamedTuple):
    '''
    Вспомогательный кортеж, для хранения лога.
    '''
    mouth: str
    day: str
    time: str 
    pc_name: str
    service_name: str
    message: str

    def get_data(self) -> Log_categories:
        '''
        Конвертирует в картеж категорий, объединяя месяц, день и время в один элемент.
        '''
        return Log_categories(f"{self.mouth} {self.day} {self.time}", self.pc_name, self.service_name, self.message)


def split_string_to_Log_categories(string_log: str) -> Log_categories:
    '''
    Разделим строку на данные time, pc_name, service_name, message.
    '''
    log_list = string_log.split(maxsplit=5)
    return Sub_categories(*log_list).get_data()

def get_string_log(nuber_of_string: int, list_of_log: list[str]) -> str:
    '''
    Возвращаем строку по номеру.
    '''
    return list_of_log[nuber_of_string]

def get_number_from_user(len_logs: int) -> int:
    result = input("Введите номер интересующего вас лога\n")
    if result.isdigit() and int(result) > -1 and int(result) < len_logs:
        return int(result)
    else:
        return None

def list_to_dict(list_of_log: list[str]) -> dict[str:str]:
    '''
    Алгоритм заполнения словаря.
    '''
    number_of_sring = None
    while not number_of_sring: #Пока пользователь не введёт число
        number_of_sring: int = get_number_from_user(len(list_of_log))
        if number_of_sring is 0: #Это лечит ошибку, когда нельзя было вызвать 0й лог
            break

    one_log = get_string_log(number_of_sring, list_of_log)
    log_categories = split_string_to_Log_categories(one_log)
    time, pc_name, service_name, message = log_categories
    log = {'time': time, 'pc_name': pc_name, 'service_name': service_name, 'message': message}
    return log

def format_dict_log(log: dict) -> str:
    '''
    Форматирует словарь в строку вида <имя компьютера>: <сообщение>
    '''
    return f"{log['pc_name']}: {log['message']}"

if __name__ == "__main__":
    print(format_dict_log(list_to_dict(list_of_log)))