from pathlib import Path
import subprocess

Run_path = Path(r"C:\Users\JIIN14400821\AppData\Local\Programs\BGNSAT\resources\static\bgn-cli\bgn-cli.exe")
output_path=r"D:\Kesavan\pytest_automation\out"
image_path=r"D:\Kesavan\Binarys\Kirkstone\iMX6SX\u-boot-sd.imx"

user_cmd_value=[
    ("--debug","--out",f"{output_path}","pkitree"),
    ("--debug","--out",f"{output_path}","srktable"),
    ("--debug","--out",f"{output_path}","cst","--op","sign","--board","imx6sxevk","--imagefile",f"{image_path}"),
    ("--debug","--out",f"{output_path}","flash","--board","imx6sxevk","--media","SDCARD","--bootloader",f"{image_path}"),
    # ("--debug","--out",f"{output_path}","flash","--board","ueipacsx","--media","TFTP","--imagefile",f"{image_path}","--port","com1","--sip","172.21.3.52","--cip","172.21.3.53")

]
def func_run(command):
    result=subprocess.run(
        command,
        executable=Run_path,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True
    )
    print(result.stdout)
    print(result.stderr)

for keys in user_cmd_value:
    print(f">>> {Run_path} "+" ".join(keys))
    func_run(keys) 