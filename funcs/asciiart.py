from colorama import Fore
import time

def start_ascii():
    start_ascii_art_1 = '''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠄⠀⠀⠀⢠⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠋⠀⠀⠀⢠⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⢹⡄⠀⠀⠀⢸⢣⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡿⠀⢻⡻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡜⢿⣇⠀⠀⡏⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⢸⡇⠀⠈⣷⡹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⡀⠉⠓⢶⡇⢠⣧⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣴⣶⣶⣤⣄⣀⠀⠀⠀⠀⢸⡇⢸⣇⠀⠀⠸⡇⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣷⣄⢸⡇⠈⣿⡟⠳⢦⣄⡀⠀⠀⠀⠀⠉⠻⢯⡉⠙⠶⣄⠉⠳⣤⠀⠀⠸⣇⠀⢻⡀⠀⠀⢱⠀⠸⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡇⠀⢯⢷⠀⠀⠀⠉⠛⠶⣦⣄⡀⠀⠀⢳⡀⠀⠀⠳⡄⠀⠳⡄⠀⠻⣆⠀⠻⣆⠀⢸⡆⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡇⠀⢸⡌⣧⡀⠒⢦⣀⠀⠀⠀⠙⠻⢦⣀⢷⡀⠀⠀⢹⡄⠀⠹⣦⡠⢿⣿⡷⣮⣻⣾⡇⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠘⣷⠙⣿⣶⣄⡉⠳⣄⡀⠀⠀⠀⠈⠻⢷⣄⠀⠀⣿⠀⠀⠙⣶⣏⣡⣶⠿⠿⠏⢻⣄⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠶⢿⠀⠀⠸⣆⠘⢷⡙⠿⣦⡈⠳⣦⣀⠀⠀⠀⠀⠙⢧⣀⣿⠆⠀⢸⠟⢻⣿⠻⣆⠀⠀⠀⠙⢧⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠛⠛⢳⣾⡆⠀⠀⠻⡄⠈⠳⣄⠙⢿⣦⡈⠻⣧⡄⠀⠀⠀⠀⠙⢿⡆⠀⠃⠀⠉⣿⣆⢹⡄⠀⠀⠀⠈⣧⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣞⣉⣷⠀⠀⠀⠹⣄⠀⠙⢧⡀⠙⢷⣄⠘⢿⣤⡀⠀⠀⠀⠀⠻⣦⣄⠀⢸⠋⠙⣦⣿⡀⠀⠀⠀⠹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⡛⠛⠛⠻⢿⣧⡀⠀⠀⠙⢧⡀⠈⠻⣦⢤⣹⣦⠀⢻⣿⠀⠀⠀⠀⣀⣹⣏⣴⣇⠀⠀⠈⣿⡇⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠈⢹⣷⠀⠀⠈⢷⠳⡀⠀⠀⠈⠻⣄⠀⠉⢷⣭⡙⣧⠀⣹⣷⣶⢖⣫⣭⣽⣿⣅⠀⠀⣰⠟⠙⡿⣦⣤⣤⣄⣸⣷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠘⣧⠙⢦⣀⡀⠀⠙⢦⡀⠀⠙⢿⣿⣿⣏⣽⣿⣿⠟⠛⢋⣻⣿⣷⣶⡋⠀⠀⣠⠾⢿⣗⠿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣾⡿⠿⠶⠶⢶⣶⣶⣶⣿⣧⡀⠻⣿⣶⡀⠈⢳⣄⠠⣄⠀⠙⠿⣿⡟⠁⠀⡴⠋⠉⠉⠙⣧⡉⠀⠊⠀⠀⠀⢙⣷⣌⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠿⢦⡀⠀⠀⠀⠀⠀⠀⠈⠉⠙⢿⣿⣦⡀⠻⣿⣶⣤⠹⣦⠈⢷⡀⢠⡟⢿⣄⠀⠀⠀⡴⠒⠂⠉⠻⢦⡀⠀⢀⠞⠉⠙⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠞⠉⠀⠀⠀⢠⡟⠀⣀⣀⣀⣀⣀⣀⣠⡶⠛⠛⣿⣿⣷⡀⠉⠻⣿⣌⣧⠀⣿⡟⠀⠀⠙⢷⣄⣸⠁⠀⠀⠀⠠⠤⢽⣏⠛⠀⠀⣀⣼⣿⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⠿⠿⠛⠻⢿⣿⡿⠋⠀⠀⠈⠉⢿⣿⣿⣄⠀⠹⣿⣿⣿⣿⠁⠀⠀⠀⠀⠙⣿⣦⡀⣸⠀⠀⠀⠀⡬⢷⣤⣴⠁⠀⠻⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣾⡿⠟⠉⠀⠀⠀⠀⠀⠀⣠⠏⠀⠀⢀⣀⣠⠾⣿⣿⣿⣿⣄⠀⠉⠉⢻⣿⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣷⣄⣰⡄⠀⠀⠀⠹⠀⠀⠀⠛⢿⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣿⠥⢤⡀⠀⠀⠀⠀⣀⣠⡾⠃⠀⠀⠈⠉⠁⠀⠀⠀⠈⠻⣿⣿⣧⣀⣀⣘⣿⡄⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠰⡄⠀⡀⠀⢸⣷⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣼⠟⠁⠀⢀⣇⣀⣴⣶⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⠿⢿⣿⡿⠉⠻⣦⡀⠀⠀⠀⠀⠀⠻⣇⠉⠛⢿⣿⣆⠀⠀⠀⠀⣳⣠⡇⣰⣼⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠁⠀⣠⣴⠿⠛⠉⠁⠀⣰⠟⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣾⣿⡟⢿⠃⠀⠀⠙⢿⣦⡀⠀⠀⠀⠀⠙⢷⣤⣤⣿⣿⢿⡶⠤⠶⠛⣿⠛⠛⡿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡿⠋⠁⠀⠀⠀⠀⣰⠇⠀⠀⠀⠀⠀⢀⡤⠖⠛⣫⣴⣾⣿⠛⠋⠀⠸⣧⣸⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠉⠻⣿⣿⠀⢷⡀⠀⠀⢻⡆⠘⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⡟⠀⠀⠀⠀⠀⣠⣾⠋⠀⠀⠀⠀⣠⠾⠋⢀⣤⣾⣿⠛⠉⠻⣆⠀⠀⠀⠙⢿⡄⠀⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠘⣿⣧⠘⠇⠀⠀⠘⡇⠀⡇⠀⠀⠀⠀⠀
⠀⠀⠀⣴⡏⣠⡀⠀⣠⣴⣾⣿⠇⠀⠀⠀⠀⠞⠋⠀⣴⣿⣿⣿⠁⠀⠀⠀⠙⢧⡀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣧⡀⠀⠀⠐⢷⡀⣷⠀⠀⠀⠀⠀
⠀⠀⢠⣿⠟⠉⣡⣾⡿⠋⠁⡟⠀⠀⠀⠀⠀⠀⢀⣾⣿⠟⠁⢿⡆⠀⠀⠀⠀⢀⡟⠻⣍⠉⠉⠻⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣬⡇⠀⠀⠀⠈⠳⢻⡆⠀⠀⠀⠀
⠀⠀⠸⠁⢀⣾⡟⠋⠀⠀⣼⠀⠀⠀⠀⠀⠀⣠⣿⣿⠁⠀⠀⠀⠙⣦⡀⠀⠀⢸⡀⠀⢈⡷⢦⣤⣬⡿⢶⣄⡀⠀⠀⢰⣤⡀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠈⢷⠀⠀⠀⠀
⠀⠀⠀⢀⣾⠏⠀⠀⠀⣰⠇⠀⠀⠀⠀⠀⣴⣿⣿⣹⣧⠀⠀⠀⠀⠀⠉⠉⠉⠉⠻⣏⠁⠀⣠⡟⠁⠀⠀⠈⠙⠶⣄⠘⠿⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀
⠀⠀⠀⣿⠃⠀⠀⢀⣼⡟⠀⠀⠀⠀⠀⢰⣿⡿⠁⠀⠘⢧⡀⠀⠀⠀⠘⢷⣀⣀⣤⠾⢿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠈⠹⣦⡀⠉⠳⣦⡀⠀⠀⠀⠀⠀⢴⡏⠉⠙⠶⠄⠘⡗⠶⡄
⠀⠀⢸⣇⡴⢶⣠⣾⣿⡇⠀⠀⠀⠀⢰⣿⣿⠃⠀⠀⠀⠀⠉⠛⢶⠶⠶⠞⢷⠀⠀⣰⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠙⢳⣄⠀⠀⠀⠈⣿⣄⠀⠀⠀⠀⠀⠀⣿
⠀⠀⣼⠟⢀⣾⡿⠋⣸⡇⠀⠀⠀⠀⣼⣿⠹⣇⠀⠀⠀⠀⠀⠀⠈⣆⠀⣀⣨⠟⠋⣽⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⠠⡀⠙⣧⡀⠀⢰⣿⣿⣆⠀⠀⠀⠀⠀⢻
⠀⢀⡏⢀⣾⡟⠀⠀⣿⠃⠀⠀⠀⢸⣿⡿⠶⠛⠷⣤⣀⣀⣀⣀⣠⢿⡟⠉⠁⠀⣼⡿⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣽⡄⠸⣇⠀⠘⠞⢿⣿⠤⠶⠂⡔⢠⠟
⠀⠀⠀⣾⡟⠀⠀⢰⡿⠀⠀⠀⠀⣿⡟⠀⠀⠀⠀⠀⠉⢹⡏⠁⠀⠈⢷⡤⠤⢴⣿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⠻⣄⡀⠀⠶⠏⠀⠀⠀⡇⣸⠀
⠀⠀⢸⣿⠁⠀⠀⢸⡇⠀⠀⠀⢰⣿⠻⣄⠀⠀⠀⠀⠀⠈⢷⣀⣤⠔⠋⠀⠀⢰⣿⠃⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣄⠈⠛⠲⣤⡀⠀⣀⡼⣿⠏⠀
⠀⠀⣼⡇⠀⠀⠀⢸⡇⠀⠀⠀⣼⣿⠴⠚⠓⢤⣄⣀⣀⣤⠴⣯⡀⠀⠀⠀⠀⣼⣿⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠦⣤⠬⢿⣦⣅⡿⠋⠀⠀
⠀⠀⣿⣴⠞⠛⢳⣼⡇⠀⠀⢠⣿⠏⠀⠀⠀⠀⠈⢹⡍⠀⠀⠈⢳⣤⣤⣴⠞⢻⡏⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠀⠀⠀⠀
⠀⢐⡿⠁⠀⠀⣾⣿⡇⠀⠀⣸⣿⡀⠀⠀⠀⠀⠀⠀⠙⣆⣀⡤⠞⠁⠀⠀⠙⢿⡇⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⡇⠀⠀⣼⣿⢻⣇⠀⠀⣿⣿⠓⢤⣀⠀⠀⠀⢀⣤⠿⣯⠀⠀⠀⠀⠀⢀⣾⡇⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠁⠀⢸⣿⠃⢘⣿⠀⠀⣿⣿⠶⠋⠉⠛⠛⣿⠉⠁⠀⠙⢷⣤⣀⣠⣴⠊⣻⡇⠀⠀⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⡟⠀⠈⣿⠀⢸⣿⡟⠀⠀⠀⠀⠀⠘⠦⣀⢀⣠⠟⠁⠀⠀⠈⠻⣿⡇⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⣿⢡⠞⢧⣿⠀⢸⣿⣧⡀⠀⠀⠀⠀⠀⠀⣰⣏⠀⠀⠀⠀⠀⠀⠀⢸⣷⠀⠀⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⠇⠀⣸⣿⠀⣾⣿⣍⣳⠦⢤⣀⡤⠴⠞⠁⠸⢧⡀⠀⠀⠀⠀⣠⣾⣿⡀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡿⠀⢠⣿⣿⠀⣿⡿⠉⠁⠀⠀⠹⣇⠀⠀⠀⠀⠀⣿⠷⠶⠶⠟⠻⣅⣿⡇⠀⠀⠀⠀⠈⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠃⣿⠀⣿⣇⠀⠀⠀⠀⠀⠈⠳⢤⣀⡴⠞⠁⠀⠀⠀⠀⠀⠀⣿⣇⠀⠀⠀⠀⠀⠘⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡿⢰⡟⢠⣿⣿⡄⠀⠀⠀⠀⠀⣀⣴⢿⡅⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡀⠀⠀⠀⠀⠀⠈⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⣸⡇⢸⣿⣿⡿⠓⠦⢤⣶⡛⠋⠁⠀⠙⠲⣤⣄⣀⣀⣀⣀⣴⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⢻⡇⢸⣿⠁⠀⠀⠀⠀⠈⢷⠀⠀⠀⠀⢀⣼⠟⠉⠉⠋⠉⠀⠉⠹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢁⣿⠇⢸⣿⠀⠀⠀⠀⠀⠀⠈⠳⢤⣤⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⡏⠀⣸⣿⡀⠀⠀⠀⠀⠀⠀⣠⣼⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠃⠀⣿⣿⣷⣶⣶⣶⣶⣶⡿⠋⠀⠉⠈⠙⢦⣄⣀⣀⣀⣠⣤⠶⠚⠓⠛⠛⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠷⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⡟⠀⢰⣿⣿⠿⢛⡏⠉⢻⡇⠀⠀⠀⠀⠀⠀⢀⡽⠋⠉⠉⠉⠀⠀⠀⠀⠀⠀⠘⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠷⣤⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⠃⠀⣸⣿⠉⠓⠊⠀⠀⠀⢳⡄⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣼⡿⠀⢠⣿⣿⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠟⠈⠻⣿⣷⣄⡀⠀⠀⠀⠀⠀⣀⣠⣤⠶⠶⠶⠛⠛⠛⠲⠿⠀⠀⠀⠀⠀⠀
⠀⢀⣴⣿⡇⠀⠀⣸⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⣠⡿⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⠿⠦⠤⠴⠾⠋⠁⠉⠙⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⠟⠁⣿⣀⣀⣾⡿⠿⠛⠿⢷⣶⣤⣠⣤⠴⠞⠋⠀⠀⠙⢦⣄⣀⠀⠀⠀⠀⠀⣀⣠⠶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠉⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⢉⡟⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣆⠀⠀⠀⠀⠀⢀⡴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⢦⣥⠤⠞⠋⢀⠀⠀⠀⠀⠀
    '''

    start_ascii_art_2 = '''
⠀⠀⠀⠀⠀⠀⣰⠂⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡟⢆⢠⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⡇⠹⢦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣦⣹⢸⡖⠤⢀⠀⠘⢿⠛⢔⠢⡀⠃⠣⠀⠇⢡⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠹⠀⡷⣄⠠⡈⠑⠢⢧⠀⢢⠰⣼⢶⣷⣾⠀⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠤⢖⡆⠰⡙⢕⢬⡢⣄⠀⠑⢼⠀⠚⣿⢆⠀⠱⣸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣤⡶⠮⢧⡀⠑⡈⢢⣕⡌⢶⠀⠀⣱⣠⠉⢺⡄⠀⢹⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡸⠀⠈⡗⢄⡈⢆⠙⠿⣶⣿⠿⢿⣷⣴⠉⠹⢶⢾⡆⠀⠀⠀
⠀⠀⠀⢠⠶⠿⡉⠉⠉⠙⢻⣮⡙⢦⣱⡐⣌⠿⡄⢁⠄⠑⢤⣀⠐⢻⡇⠀⠀⠀
⠀⠀⠀⢀⣠⠾⠖⠛⢻⠟⠁⢘⣿⣆⠹⢷⡏⠀⠈⢻⣤⡆⠀⠑⢴⠉⢿⣄⠀⠀
⠀⠀⢠⠞⢃⢀⣠⡴⠋⠀⠈⠁⠉⢻⣷⣤⠧⡀⠀⠈⢻⠿⣿⡀⠀⢀⡀⣸⠀⠀
⠀⠀⢀⠔⠋⠁⡰⠁⠀⢀⠠⣤⣶⠞⢻⡙⠀⠙⢦⠀⠈⠓⢾⡟⡖⠊⡏⡟⠀⠀
⠀⢠⣋⢀⣠⡞⠁⠀⠔⣡⣾⠋⠉⢆⡀⢱⡀⠀⠀⠀⠀⠀⠀⢿⡄⠀⢇⠇⠀⠀
⠀⠎⣴⠛⢡⠃⠀⠀⣴⡏⠈⠢⣀⣸⣉⠦⣬⠦⣀⠀⣄⠀⠀⠈⠃⠀⠀⠙⡀⠀
⠀⡸⡁⣠⡆⠀⠀⣾⠋⠑⢄⣀⣠⡤⢕⡶⠁⠀⠀⠁⢪⠑⠤⡀⠀⢰⡐⠂⠑⢀
⠀⠏⡼⢋⠇⠀⣸⣟⣄⠀⠀⢠⡠⠓⣿⠇⠀⠀⠀⠀⠀⠑⢄⡌⠆⢰⣷⣀⡀⢸
⠀⣸⠁⢸⠀⢀⡿⡀⠀⠈⢇⡀⠗⢲⡟⠀⠀⠀⠀⠀⠀⠀⠀⠹⡜⠦⣈⠀⣸⡄
⠀⣧⠤⣼⠀⢸⠇⠉⠂⠔⠘⢄⣀⢼⠃⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠚⠳⠋⠀
⠐⠇⣰⢿⠀⣾⢂⣀⣀⡸⠆⠁⠀⣹⠀⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡏⣸⠀⣟⠁⠀⠙⢄⠼⠁⠈⢺⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⡏⣸⢰⡯⠆⢤⠔⠊⢢⣀⣀⡼⡇⠀⠹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⢻⢸⡇⠀⠀⠑⣤⠊⠀⠀⠈⣧⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠸⣼⢸⠟⠑⠺⡉⠈⢑⠆⠠⠐⢻⡄⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡟⣸⡀⠀⠀⣈⣶⡁⠀⠀⠀⢠⢻⡄⠀⠀⠀⠑⠤⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⢰⠁⣿⡿⠟⢏⠁⠀⢈⠖⠒⠊⠉⠉⠹⣄⠀⠀⠀⠀⠀⠈⠑⠢⡀⠀⠀⠀
⠀⣀⠟⢰⡇⠀⠀⠈⢢⡴⠊⠀⠀⠀⠀⠀⣸⢙⣷⠄⢀⠀⠠⠄⠐⠒⠚⠀⠀⠀
⠘⠹⠤⠛⠛⠲⢤⠐⠊⠈⠂⢤⢀⠠⠔⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠣⢀⡀⠔⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    '''
    
    start_ascii_name = '''
  _    _           _           _       _____         _____     _____                       
 | |  | |         | |         ( )     |  __ \  ___  |  __ \   / ____|                      
 | |__| |_   _  __| |_ __ ___ |/ ___  | |  | |( _ ) | |  | | | |  __  __ _ _ __ ___   ___  
 |  __  | | | |/ _` | '__/ _ \  / __| | |  | |/ _ \/\ |  | | | | |_ |/ _` | '_ ` _ \ / _ \ 
 | |  | | |_| | (_| | | | (_) | \__ \ | |__| | (_>  < |__| | | |__| | (_| | | | | | |  __/ 
 |_|  |_|\__, |\__,_|_|  \___/  |___/ |_____/ \___/\/_____/   \_____|\__,_|_| |_| |_|\___| 
          __/ |                                                                            
         |___/                                                                            
'''

    print(Fore.CYAN + start_ascii_name)
    time.sleep(2)
    print(Fore.RED + start_ascii_art_2)

if __name__ == "__main__":
    start_ascii()