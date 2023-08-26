import datetime
import winsound


def alarm(timing):
    altime = str(datetime.datetime.now().strptime(timing,"%I:%M %p"))
    altime = altime[11:-3]
    horeal = altime[:2]
    horeal = int(horeal)
    mireal = altime[3:5]
    mireal = int(mireal)
    print(f"Alarm has been set for {timing}")

    while True:
        if horeal == datetime.datetime.now().hour:
            if mireal == datetime.datetime.now().minute:
               print("Alarm is running")
               winsound.PlaySound("abc", winsound.SND_LOOP)

            elif mireal < datetime.datetime.now().minute:
                 break


if __name__ == '__main__':
    alarm('05:11 PM')
