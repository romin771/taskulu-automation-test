import logging
import inspect


def Custom_logger(loglevel=logging.DEBUG):  #assign default value // we are providing in case we forget to provide from outside
    # one of the benefits of inspect is : we can get the name of the method where This custom_logger method is called from there .
    loggerName = inspect.stack()[1][3]

    #defice a loggir
    logger = logging.getLogger(loggerName)  #we know from where the log is comming //
    #log by default to Debug
    logger.setLevel(logging.DEBUG)


    #find handler
    #fileHandler = logging.FileHandler(filename="{0}.log".format(loggerName), mode="w") #if we user this for everyclass we have a log file
    fileHandler = logging.FileHandler(filename="automation.log".format(loggerName), mode="a") # a = append
    fileHandler.setLevel(loglevel) #the loglevel tht user is providing


    #define fomrmatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)

    #add handler to logger
    logger.addHandler(fileHandler)

    return logger