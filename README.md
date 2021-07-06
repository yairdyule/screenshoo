# screenshoo

### 🚨 ⚠️  Under development! Don't trust screenshoo with the nuclear codes!!

## Motivation 
Have you ever, having spent a day blithely `cmd+shift+4'ing`, come back to your desktop only to be greeted by an atrocious, cluttered desktop?! Did *you* have far too much time on your hands this morning?

## Enter screenshoo.
Screenshoo is a (probably over-engineered, probably broken) solution to this untenable state of affairs. It will move all files with names like "Screen s" (lazy) from `/Desktop` to `/Desktop/!#&$ screenshots`

## Config
You'll need to `pip3 install` the `os`, `schedule`, and `time` modules as necessary.

The only other config, as far as I'm aware, is to modify the following lines in `screenshoo.py`:

`path = "/Users/jaredjewell/Desktop" #path to your desktop`
`dirname = "!#&$ screenshots"        #name of the dump dir`

## Usage
In my case, I just had to `nohup python3 screenshoo.py &`

- `nohup` will continue running screenshoo even if you exit your shell.
- `&` runs it as a background process.

There's probably a better way to automate all of this, so please let me know if this is a reinvention of the wheel in any way.

You'll need to remember to redo this on startup, but your ugly desktop should serve as a cheeky reminder to do so ;)

## Issues
Doubt anyone will see this so no sweat here. Just kidding. If you *do* see this, and find a bug/see somewhere we can improve screenshoo, please PR :D <3
