import picar_4wd as fc
import time

speed = 30

def main():
    while True:
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        tmp = scan_list[3:7]
        print("Full Range: ", scan_list)
        print("Scanned Area: ", tmp)

        if tmp != [2,2,2,2]:
            fc.backward(speed/10)
            time.sleep(1)
            fc.turn_right(speed)
            time.sleep(1)
            fc.stop()
        else:
            fc.forward(speed)

if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()
