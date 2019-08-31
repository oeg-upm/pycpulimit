# pycpulimit
Limit CPU usage for your processes by name using `cpulimit`

*tested on MacOS only* but should work with linux as well.

# How to Install it
1. Download `cpulimit` (`brew install cpulimit` for Mac)
2. Download this application (https://github.com/oeg-upm/pycpulimit/releases/tag/v1.0)
3. Go to the extracted folder of this app using the terminal (e.g., `cd /Users/YOUR-USERNAME/pycpulimit`)
4. Make the application executable `chmod 666 pycpulimit.*`
5. Add the application to the PATH variable. You can append it to (in Mac it is`/Users/YOUR-USERNAME/.bash_profile`)

*Substitute `YOUR-USERNAME` with your actual username*


# How to use it
Go to the terminal and write this `pycpulimit.sh YOUR-APP 40`. 
We are restricting the app to have by max 40% of the CPU.

*Substitute `YOUR-APP` with the application name you like to restrict the cpu access to*

