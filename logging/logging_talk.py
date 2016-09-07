

import sys


try:
    print('Trying to read name!')
    name = sys.argv[1]
except:
    print('Usage: logging_talk.py [name]')
    sys.exit(1)

print('Read name!')
print('Hi {}!'.format(name))







#import logging


## logging.debug('Debug message')
## logging.info('Info message')
#logging.warning('Warning message')
#logging.error('Error message')
#logging.critical('Critical message')







#import logging


#logging.debug('Debug message')
#logging.info('Info message')
#logging.warning('Warning message')
#logging.error('Error message')
#logging.critical('Critical message')







#import logging


#logging.basicConfig(level=logging.INFO)
#logging.debug('Debug message')
#logging.info('Info message')
#logging.warning('Warning message')
#logging.error('Error message')
#logging.critical('Critical message')








#import logging


#logging.basicConfig(format='%(levelname)s %(message)s', level=logging.INFO)
#logging.debug('Debug message')
#logging.info('Info message')
#logging.warning('Warning message')
#logging.error('Error message')
#logging.critical('Critical message')




#logging.basicConfig(level=logging.DEBUG)
#try:
#    logging.debug('Trying to read name!')
#    name = sys.argv[1]
#except:
#    logging.error('Usage: logging_talk.py [name]')
#    sys.exit(1)
#
#logging.info('Read name!')
#logging.info('Hi {}!'.format(name))

