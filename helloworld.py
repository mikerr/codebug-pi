import time
import codebug_i2c_tether

with codebug_i2c_tether.CodeBug() as codebug:

        message = 'Hello world!'
        for i in range(len(message) * 6):
                time.sleep(0.05)
                codebug.write_text(-i, 0, message)

