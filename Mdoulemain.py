from Module_Logger import setup_logger
logger = setup_logger(log_file="application.log", level="DEBUG")
def main():
    logger.info("Application started.")
    try:
        logger.debug("Performing a division operation.")
        result = 10 / 2
        logger.info(f"Operation successful. Result: {result}")
        logger.debug("Attempting division by zero.")
        result = 10 / 0
    except ZeroDivisionError as e:
        logger.error("An error occurred: Division by zero.")
        logger.exception(e)
    finally:
        logger.warning("Application is closing.")
if __name__ == "__main__":
    main()
