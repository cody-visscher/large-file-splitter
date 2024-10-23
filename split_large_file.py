if __name__ == "__main__":
    filename = input('Path to large file: ')
    i = 1
    break_file = open(f'{filename}{i}', 'w')
    with open(filename, 'r') as file:
        while True:
            s = file.read(128000000)
            break_file.write(s)
            print(f'{filename}{i} written.')
            i += 1
            break_file.close()
            if len(s) < 128000000:
                break
            break_file = open(f'{filename}{i}','w')
    input('Press enter to close.')