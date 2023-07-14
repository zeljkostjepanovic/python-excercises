import time

start = time.time()

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()
        
        
# A List of Items
num_of_aliens = range(0, 300000)

# Initial call to print 0% progress
printProgressBar(0, len(num_of_aliens), prefix = 'Working:', suffix = 'Done', length = 50)
aliens = []
# Create an army of aliens
for alien_num in num_of_aliens:
    # Do stuff...
    new_alien = {}
    new_alien['color'] = 'green'
    new_alien['points'] = 5
    new_alien['x'] = 20 * alien_num
    new_alien['y'] = 0
    aliens.append(new_alien)
    # Update Progress Bar
    printProgressBar(alien_num + 1, len(num_of_aliens), prefix = 'Working: ', suffix = 'Done', length = 50)

# How many?
print(len(aliens))

end = time.time()
print(end - start)