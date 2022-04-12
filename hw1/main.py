from datetime import datetime

def main():
    name = 'Andriy Sultanov'
    current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print(f'{name}\n{current_time}')
	
if __name__ == '__main__':
    main()
