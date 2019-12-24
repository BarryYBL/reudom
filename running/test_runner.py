# coding=utf-8
import os
import time
import logging
import unittest
from .HTMLTestRunner import HTMLTestRunner

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


reudom_str = """
                     _                 
                    | |                
  _ __ ___ _   _  __| | ___  _ __ ___  
 | '__/ _ | | | |/ _` |/ _ \| '_ ` _ \ 
 | | |  __| |_| | (_| | (_) | | | | | |
 |_|  \___|\__,_|\__,_|\___/|_| |_| |_|                             
 --------------------------------------
                            @itest.info
"""

def main(path=None,
         title="Reudom Test Report",
         description="Test case execution",
         debug=False,
         rerun=0,
         save_last_run=False):
    """
    runner test case
    :param path:
    :param title:
    :param description:
    :param debug:
    :param rerun:
    :param save_last_run:
    :return:
    """

    if path is None:
        suits = unittest.defaultTestLoader.discover(os.getcwd())
    else:
        if len(path) > 3:
            if path[-3:] == ".py":
                if "/" in path:
                    path_list = path.split("/")
                    path_dir = path.replace(path_list[-1], "")
                    suits = unittest.defaultTestLoader.discover(path_dir, pattern=path_list[-1])
                else:
                    suits = unittest.defaultTestLoader.discover(os.getcwd(), pattern=path)
            else:
                suits = unittest.defaultTestLoader.discover(path)
        else:
            suits = unittest.defaultTestLoader.discover(path)

    if debug is False:
        for filename in os.listdir(os.getcwd()):
            if filename == "reports":
                break
        else:
            os.mkdir(os.path.join(os.getcwd(), "reports"))

        now = time.strftime("%Y_%m_%d_%H_%M_%S")
        report = os.path.join(os.getcwd(), "reports", now + "_result.html")

        with(open(report, 'wb')) as fp:
            runner = HTMLTestRunner(stream=fp, title=title, description=description)
            print(reudom_str)
            runner.run(suits, rerun=rerun, save_last_run=save_last_run)
        print("generated html file: file:///{}".format(report))
    else:
        runner = unittest.TextTestRunner(verbosity=2)
        logger.info("reudom run test 🛫🛫!")
        print(reudom_str)
        runner.run(suits)
        logger.info("End of the test 🔚!")


if __name__ == '__main__':
    main()

